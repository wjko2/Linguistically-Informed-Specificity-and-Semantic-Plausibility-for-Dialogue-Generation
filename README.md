
Code for Wei-Jen Ko, Greg Durrett and Junyi Jessy Li, "Training command:
 and Semantic Plausibility for Dialogue Generation", The AAAI Conference on Artificial Intelligence (NAACL), 2019

This is the code for our response generation model.

**Citation:**
```
@InProceedings{ko2019linguistically,
  author    = {Ko, Wei-Jen and Durrett, Greg and Li, Junyi Jessy},
  title     = {Linguistically-Informed Specificity and Semantic Plausibility for Dialogue Generation},
  booktitle = {NAACL},
  year      = {2019},
}
```

## Dependencies
-Pytorch (Tested on 0.3.1)
This code is based on [OpenNMT](https://github.com/OpenNMT/OpenNMT-py)

## Commands For Running 
Data preprocessing:

python preprocess.py -train_src data/train_prompt.txt -train_tgt data/train_response.txt -valid_src data/valid_prompt.txt -valid_tgt data/valid_response.txt -save_data data/personachat

Training:

python traingn.py -data data/personachat -save_model model -gpuid 0 -rnn_size 500 -batch_size 64 -epochs 100 -optim adam -learning_rate 0.001 -learning_rate_decay 0.5 -dropout 0.2 -global_attention mlp 

Testing:

python translategn.py -model model_acc_XXX_ppl_XXX_eX.pt  -src data/test.txt -output output.txt  -verbose -block_ngram_repeat 3 

## Specificity metrics
For Linguistic informed specificity, we use [our system](https://github.com/wjko2/Domain-Agnostic-Sentence-Specificity-Prediction).

For computing perplexity, we use [the RNNLM toolkit](http://www.fit.vutbr.cz/~imikolov/rnnlm/).


