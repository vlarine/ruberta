# Russian RoBERTa

Training a Rossian RoBERTA model using:
* [YouTokenToMe](https://github.com/VKCOM/YouTokenToMe) as a tokenizer.
* [Fairseq](https://github.com/pytorch/fairseq) toolkit

## Reqiurements

* pytorch
* youtokentome
* tensorboard for training visualisation

## Training

1. Copy a YouTokenToMe tokenizer class and token names changes in Fairseq's dictionary class: 

```bash
$ cp -fr fairseq_patch/* fairseq/
```

2. Train a tokenizer model and split data on train/valid/test (change paths if needed):

```bash
$ python3 ./scripts/run_pretraining.py
```

3. Encode and binarize the data:

```bash
$ ./scripts/run_encoding.sh
```

4. Start training:

```bash
$ ./scripts/run_train_16.sh
```

