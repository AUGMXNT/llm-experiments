Experiments:

# LangChain  Experiments

LangChain
https://blog.langchain.dev/using-chatgpt-api-to-evaluate-chatgpt/
https://twitter.com/jamescodez/status/1645464631513845760

https://github.com/jerryjliu/llama_index

# Extensions
Cache
https://github.com/zilliztech/gptcache

Memory Plugin
https://github.com/openai/chatgpt-retrieval-plugin#memory-feature

Plugin parsing
https://twitter.com/hwchase17/status/1640171938470563840
https://python.langchain.com/en/latest/modules/agents/tools/examples/chatgpt_plugins.html
https://python.langchain.com/en/latest/modules/agents/tools/examples/chatgpt_plugins.html

PDF Search
https://twitter.com/sergeykarayev/status/1640572813827518464

https://github.com/hyperonym/basaran
Basaran is an open-source alternative to the OpenAI text completion API. It provides a compatible streaming API for your Hugging Face Transformers-based text generation models.

The open source community will eventually witness the Stable Diffusion moment for large language models (LLMs), and Basaran allows you to replace OpenAI's service with the latest open-source model to power your application without modifying a single line of code.

# Coding Plugins

https://github.com/features/copilot/
https://github.com/ravenscroftj/turbopilot
https://github.com/ravenscroftj/fauxpilot
https://github.com/catid/supercharger

https://huggingface.co/blog/stackllama
https://huggingface.co/spaces/trl-lib/stack-llama

# Real-world Benchmarks
* API to allow questions to be asked, answers to be timed, metadata stored (version, date, etc)
* UI
  * Add questions, run benchmarks
  * Allow rating (correct/incorrect, ranking)
  * Allow rerun, running multiple times (versions), adjust parameters
* Summarize rankings
* Allow judging?
* See: https://github.com/spenceryonce/LLMeval ; pyllms has eval as well

# Character Stuff
Vicuna works best w/ llama.cpp directly?
https://www.reddit.com/r/LocalLLaMA/comments/12ilu7b/comment/jfuzt0y/?utm_source=reddit&utm_medium=web2x&context=3

Emily is a character defined with the prompt template shown above. It's copy-pasted from koboldcpp, but with some custom additions ;) Just fill the template in the way you want your AI character will be like.

Here is an example AI gangster character prompt:

[Character: Tony; species: Human; age: 34; gender: male; physical appearance: rough, tattooed, drug dealer, gangster, pimp; personality: aggressive, swearing; description: Tony has just got out of prison for drug dealing, pimping and stealing cars. You've known each other since kids, when your ways parted.]

[You meet accidentally on the street where you suddenly recognize him. Following is a dialog between you and Tony]

[Tags: Gangster, Drugs, Guns, Whores, Bitches, Cars, Sluts, Swearing.]

You: Yo man! Tony - is that you ? Couldn't recognize you, maan !

Tony: Get out of my way !!! What, Stan ? Is that you ?! You fucken' bastard !
