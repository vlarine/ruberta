
if true; then

    python3 multiprocessing_bpe_encoder.py \
        --vocab-bpe ../data/vocab_30000.bpe \
        --inputs ../data/test.txt \
        --outputs ../data/test_split.bpe \
        --max-len 512 \
        --workers 10

    python3 multiprocessing_bpe_encoder.py \
        --vocab-bpe ../data/vocab_30000.bpe \
        --inputs ../data/valid.txt \
        --outputs ../data/valid_split.bpe \
        --max-len 512 \
        --workers 10

    python3 multiprocessing_bpe_encoder.py \
        --vocab-bpe ../data/vocab_30000.bpe \
        --inputs ../data/train.txt \
        --outputs ../data/train_split.bpe \
        --max-len 512 \
        --workers 10

fi


if true; then

    python3 preprocess.py \
        --only-source \
        --trainpref ../data/train_split.bpe \
        --validpref ../data/valid_split.bpe \
        --testpref ../data/test_split.bpe \
        --destdir ../data/bpe \
        --joined-dictionary \
        --workers 10

fi
