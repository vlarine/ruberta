
if false; then

    python3 multiprocessing_bpe_encoder.py \
        --vocab-bpe ../data/vocab_50000.bpe \
        --inputs ../data/test.txt \
        --outputs ../data/test_split50.bpe \
        --max-len 512 \
        --workers 10

    python3 multiprocessing_bpe_encoder.py \
        --vocab-bpe ../data/vocab_50000.bpe \
        --inputs ../data/valid.txt \
        --outputs ../data/valid_split50.bpe \
        --max-len 512 \
        --workers 10

    python3 multiprocessing_bpe_encoder.py \
        --vocab-bpe ../data/vocab_50000.bpe \
        --inputs ../data/train.txt \
        --outputs ../data/train_split50.bpe \
        --max-len 512 \
        --workers 10

fi


if true; then

    python3 preprocess.py \
        --only-source \
        --trainpref ../data/train_split50.bpe \
        --validpref ../data/valid_split50.bpe \
        --testpref ../data/test_split50.bpe \
        --destdir ../data/bpe50 \
        --joined-dictionary \
        --workers 10

fi
