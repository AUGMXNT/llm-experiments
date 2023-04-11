We use the [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) to evaluate `text-davinci-003`

We install this with `pip install lm-eval` - it installs a lot of stuff (and requires a bunch of dependencies that aren't automatically installed like `pytest` and a few others). It also takes quite a while (about an hour?) to download the tests even on a fast connection.

We run it in a shell script like so:
```
python main.py \
    --model gpt3 \
    --model_args engine=text-davinci-003 \
    --tasks lambada_openai,lambada_standard,hellaswag,winogrande,piqa,coqa \
    --check_integrity
```

While `gpt-3.5-turbo` is supposed to perform on par with Instruct Davinci, you can only use it with the Chat API. It's cost is $0.002 / 1K tokens, while Davinci is $0.0200 / 1K tokens. At these prices, running the above eval cost ~$90.77 (~4.5M tokens).

Results:
```
gpt3 (engine=text-davinci-003), limit: None, provide_description: False, num_fewshot: 0, batch_size: None
|      Task      |Version| Metric |Value |   |Stderr|
|----------------|------:|--------|-----:|---|-----:|
|winogrande      |      0|acc     |0.7553|±  |0.0121|
|lambada_openai  |      0|ppl     |2.6089|±  |0.0576|
|                |       |acc     |0.7444|±  |0.0061|
|piqa            |      0|acc     |0.8319|±  |0.0087|
|                |       |acc_norm|0.8384|±  |0.0086|
|hellaswag       |      0|acc     |0.6780|±  |0.0047|
|                |       |acc_norm|0.8333|±  |0.0037|
|lambada_standard|      0|ppl     |3.0489|±  |0.0754|
|                |       |acc     |0.7075|±  |0.0063|
|coqa            |      1|f1      |0.7589|±  |0.0139|
|                |       |em      |0.5843|±  |0.0196|
```

Fabrice Ballard has run this set of evals on many of the models (and quantizations!) that we'd want to compare with: https://bellard.org/ts_server/ Here's where `text-davinci-003` sits:

| Model              | RAM | lambada (ppl) | lambada (acc) | hellaswag (acc_norm) | winogrande (acc) | piqa (acc) | coqa (f1) | average |
|--------------------|-----|---------------|---------------|----------------------|------------------|------------|-----------|---------|
| llama_65B_q4       | 39  | 2.76          | 78.50%        | 83.90%               | 76.60%           | 81.40%     | 83.20%    | 80.70%  |
| llama_30B_q8       | 36  | 2.853         | 77.70%        | 82.70%               | 76.30%           | 80.30%     | 80.40%    | 79.50%  |
| llama_30B_q4       | 20  | 2.877         | 77.50%        | 82.40%               | 75.70%           | 80.20%     | 80.20%    | 79.20%  |
| *text-davinci-003* | n/a | 3.0489        | 70.75%        | 83.33%               | 75.53%           | 83.19%     | 75.89%    | 77.74%  |
| llama_13B_q8       | 15  | 3.178         | 76.50%        | 79.10%               | 73.20%           | 79.10%     | 77.10%    | 77.00%  |
| llama_13B_q4       | 8   | 3.13          | 77.10%        | 78.60%               | 72.20%           | 78.30%     | 77.80%    | 76.80%  |
| flan_t5_xxl_q8     | 13  | 3.049         | 77.80%        | 72.10%               | 75.10%           | 77.80%     | 73.10%    | 75.20%  |
| llama_7B           | 14  | 3.463         | 73.60%        | 76.20%               | 70.40%           | 78.10%     | 75.40%    | 74.70%  |
| llama_7B_q8        | 8   | 3.453         | 73.70%        | 76.10%               | 70.20%           | 78.00%     | 75.50%    | 74.70%  |
| llama_7B_q4        | 5   | 3.549         | 73.20%        | 75.50%               | 70.40%           | 78.00%     | 74.70%    | 74.40%  |
| flan_t5_xxl_q4     | 7   | 3.01          | 77.70%        | 71.50%               | 73.40%           | 77.60%     | 71.80%    | 74.40%  |
| opt_66B_q4         | 40  | 3.308         | 73.40%        | 74.40%               | 68.40%           | 78.50%     | 75.00%    | 73.90%  |
| opt_30B_q8         | 34  | 3.628         | 71.60%        | 72.30%               | 68.20%           | 77.70%     | 71.40%    | 72.30%  |
| gptneox_20B_q8     | 23  | 3.659         | 72.60%        | 71.30%               | 65.80%           | 77.30%     | 72.90%    | 72.00%  |
| gptneox_20B        | 43  | 3.657         | 72.60%        | 71.40%               | 65.50%           | 77.50%     | 73.30%    | 72.00%  |
| fairseq_gpt_13B_bf4| 9   | 3.646         | 71.20%        | 72.50%               | 67.60%           | 77.40%     | 70.60%    | 71.90%  |
| fairseq_gpt_13B    | 27  | 3.567         | 71.90%        | 72.70%               | 67.50%           | 77.60%     | 70.10%    | 71.90%  |
| fairseq_gpt_13B_bf8| 15  | 3.565         | 71.80%        | 72.70%               | 67.20%           | 77.70%     | 70.00%    | 71.90%  |
| opt_30B_q4         | 19  | 3.656         | 71.50%        | 72.10%               | 68.00%           | 77.40%     | 69.90%    | 71.80%  |
| gptneox_20B_q4     | 13  | 3.711         | 72.00%        | 69.30%               | 64.80%           | 76.70%     | 70.80%    | 70.70%  |


We can add in other sources of `lm-eval` results like:
* https://www.aleph-alpha.com/luminous-performance-benchmarks

`claude-instant-v1` should perform on about the same level as `gpt-3.5-turbo`:
* https://github.com/kagisearch/pyllms/tree/main#benchmarks

See also:
* https://wandb.ai/wandb_gen/llm-evaluation/reports/Evaluating-Large-Language-Models-LLMs-with-Eleuther-AI--VmlldzoyOTI0MDQ3

---
Full JSON results:

```json
{
  "results": {
    "winogrande": {
      "acc": 0.755327545382794,
      "acc_stderr": 0.012082125654159738
    },
    "lambada_openai": {
      "ppl": 2.6088786186020605,
      "ppl_stderr": 0.05758481395456482,
      "acc": 0.7444207257908014,
      "acc_stderr": 0.006076928367674913
    },
    "piqa": {
      "acc": 0.8318824809575626,
      "acc_stderr": 0.008725350811241683,
      "acc_norm": 0.838411316648531,
      "acc_norm_stderr": 0.008587751299447739
    },
    "hellaswag": {
      "acc": 0.6779525990838479,
      "acc_stderr": 0.004663060828376781,
      "acc_norm": 0.8333001394144592,
      "acc_norm_stderr": 0.003719459738399207
    },
    "lambada_standard": {
      "ppl": 3.0489055102298397,
      "ppl_stderr": 0.07538504687766555,
      "acc": 0.7075490005821852,
      "acc_stderr": 0.006337484186544313
    },
    "coqa": {
      "f1": 0.7588553465756964,
      "f1_stderr": 0.013933087384831054,
      "em": 0.5843333333333334,
      "em_stderr": 0.01957429935602932
    }
  },
  "versions": {
    "winogrande": 0,
    "lambada_openai": 0,
    "piqa": 0,
    "coqa": 1,
    "hellaswag": 0,
    "lambada_standard": 0
  },
  "config": {
    "model": "gpt3",
    "model_args": "engine=text-davinci-003",
    "num_fewshot": 0,
    "batch_size": null,
    "device": null,
    "no_cache": false,
    "limit": null,
    "bootstrap_iters": 100000,
    "description_dict": {}
  }
}
```

