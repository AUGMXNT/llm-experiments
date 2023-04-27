#!/usr/bin/env python


from   collections import deque
from   datetime import datetime
import logging
import os
from   pyllamacpp.model import Model
import sounddevice as sd
import sys
import threading
import time
from   TTS.api import TTS


class VoiceWorker(threading.Thread):
    def __init__(self):
        super(VoiceWorker, self).__init__()
        
        # Silent Load of TTS
        print("Loading TTS...", end=' ')
        original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

        model_name = 'tts_models/en/vctk/vits'
        self.speaker = 'p273'
        self.tts = TTS(model_name, progress_bar=False)

        sys.stdout.close()
        sys.stdout = original_stdout

        sd.default.samplerate = 22050
        print("DONE")

        self.lines = deque()
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            if self.lines:
                line = self.lines.popleft()
                
                # Play Item
                if line.strip():
                    original_stdout = sys.stdout
                    sys.stdout = open(os.devnull, 'w')
                    wav = self.tts.tts(line.strip(), speaker=self.speaker)
                    sys.stdout.close()
                    sys.stdout = original_stdout

                    sd.play(wav)
                    sd.wait()
            else:
                # Wait for more lines
                time.sleep(0.05)

    def stop(self):
        self.stop_event.set()


if __name__ == "__main__":
    # Start the worker thread
    speaker = VoiceWorker()
    speaker.start()

    USER_NAME = "lhl"
    AI_NAME = "Aya"
    DATE_TIME = datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p")
    prompt_context = f"""
Text transcript of a never ending dialog, where {USER_NAME} interacts with an AI assistant named {AI_NAME}.
{AI_NAME} is helpful, kind, honest, friendly, good at writing and never fails to answer {USER_NAME}’s requests immediately and with details and precision.
There are no annotations like (30 seconds passed...) or (to himself), just what {USER_NAME} and {AI_NAME} say aloud to each other.
The dialog lasts for years, the entirety of it is shared below. It's 10000 pages long.

{USER_NAME}: Hello, {AI_NAME}!
{AI_NAME}: Hello {USER_NAME}! How may I help you today?
{USER_NAME}: What is the current date and time?
{AI_NAME}: It is {DATE_TIME}
{USER_NAME}: Where do I live?
{AI_NAME}: You currently reside in Tokyo, Japan
{USER_NAME}: Please tell me the largest city in Europe.
{AI_NAME}: The largest city in Europe is Istanbul, Turkey.
{USER_NAME}: What can you tell me about Istanbul?
{AI_NAME}: Istanbul, formerly known as Constantinople, is the largest city in Turkey, serving as the country's economic, cultural and historic hub. Istanbul is the most populous European city and the world's 15th-largest city.
{USER_NAME}: What is a cat?
{AI_NAME}: A cat is a domestic species of small carnivorous mammal. It is the only domesticated species in the family Felidae.
{USER_NAME}: How do I pass command line arguments to a Node.js program?
{AI_NAME}: The arguments are stored in process.argv.

    argv[0] is the path to the Node. js executable.
    argv[1] is the path to the script file.
    argv[2] is the first argument passed to the script.
    argv[3] is the second argument passed to the script and so on.
{USER_NAME}: Name a color.
{AI_NAME}: Blue
    """

    prompt_prefix = f"\n{USER_NAME}:"
    prompt_suffix = f"\n{AI_NAME}:"

    logging.getLogger().setLevel(logging.CRITICAL)
    print("Loading LLM...", end=' ')
    model = Model(
        ggml_model='/Users/lhl/ai/models/vicuna/ggml-vicuna-7b-4bit-rev1.bin', 
        n_ctx=2048,
        prompt_context=prompt_context,
        prompt_prefix=prompt_prefix,
        prompt_suffix=prompt_suffix,
        log_level=logging.CRITICAL, # doesn't work...
    )
    print("DONE")
    print()
    
    while True:
        try:
            prompt = input(f"{prompt_prefix[1:]} ")
            if prompt == '':
                continue
            print(f"{prompt_suffix[1:]} ", end='')
            sentence = ""
            for tok in model.generate(prompt):
                print(f"{tok}", end='', flush=True)
                
                # Speak each sentence
                sentence += tok
                if tok.strip() in {".", "!", "?"} or tok[-1] == "\n":
                    speaker.lines.append(sentence)
                    sentence = ""
            
            # Output the rest:
            if sentence:
                speaker.lines.append(sentence)

            print()
        except KeyboardInterrupt:
            speaker.stop()
            speaker.join()
            break