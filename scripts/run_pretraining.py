import os
import random
import youtokentome as yttm


DATA_DIR = '../data/'
ALL_FILE = '{}/all.txt'.format(DATA_DIR)
BPE_FILE = '{}/vocab_30000.bpe'.format(DATA_DIR)

if False:
    print('Train BPE model')
    yttm.BPE.train(
        data=ALL_FILE,
        vocab_size=30000,
        model=BPE_FILE,
        n_threads=4,
        coverage=0.9999,
        pad_id=1, unk_id=3, bos_id=0, eos_id=2
    )

if True:
    print('Test BPE model')
    bpe = yttm.BPE(model=BPE_FILE)
    print(bpe.vocab()[:1000])

if False:
    print('Split train/test/valid')
    with open(ALL_FILE) as f, \
         open('{}/valid.txt'.format(DATA_DIR), 'w') as wf1, \
         open('{}/test.txt'.format(DATA_DIR), 'w') as wf2, \
         open('{}/train.txt'.format(DATA_DIR), 'w') as wf3:
        write_file = 1
        print('Write to a valid file')
        for i, line in enumerate(f):
            if write_file == 1 and i > 50000 and not line.split():
                write_file = 2
                print('Write to a test file')
                continue
            elif write_file == 2 and i > 100000 and not line.split():
                write_file = 3
                print('Write to a train file')
                continue

            if write_file == 1:
                wf1.write(line)
            elif write_file == 2:
                wf2.write(line)
            else:
                wf3.write(line)

