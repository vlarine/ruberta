<img src="https://github.com/vlarine/ruberta/blob/master/img/ruberta.png" width="300px" />

# Russian RoBERTa

Training a Rossian RoBERTA model using:
* [YouTokenToMe](https://github.com/VKCOM/YouTokenToMe) as a tokenizer.
* [Fairseq](https://github.com/pytorch/fairseq) toolkit

## Reqiurements

* pytorch
* youtokentome
* tensorboard for training visualisation

## Training

1. Train a tokenizer model and split data on train/valid/test (change paths if needed):

```bash
$ python3 ./scripts/run_pretraining.py
```

2. Encode and binarize the data:

```bash
$ ./scripts/run_encoding.sh
```

3. Start training:

```bash
$ ./scripts/run_train_16.sh
```

## Pretrained models

A model trained on russian Wiki + [Taiga corpus](https://tatianashavrina.github.io/taiga_site/). Trained ~3 days on 2x1080Ti:
[RuBERTa-base, batch 256, 20k steps](https://drive.google.com/open?id=1MC-5Qy-qWq1mHMiF1D7GIsUwYLuLanmy)

F1 score on [Sber SQuAD dataset](https://github.com/vlarine/transformers-ru): 74.05


