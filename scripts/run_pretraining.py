import os
import random
import re
import youtokentome as yttm


DATA_DIR = '../data/'
ALL_FILE = '{}/all.txt'.format(DATA_DIR)
ALL_FOR_BPE_FILE = '{}/all_for_bpe.txt'.format(DATA_DIR)
BPE_FILE = '{}/vocab_50000.bpe'.format(DATA_DIR)
TMP_FILE = '{}/bpe_tmp_.txt'.format(DATA_DIR)


if False:
    print('Preprocess BPE train data')
    """
        Exclude from the dictionary tokens with the special characters at the end.
    """

    specials = ',.-"!:)(;/—«»*?=><“”–+\'][%_~#'
    re_begin = re.compile('(\S)([,.\-"!:\)\(;/—«»*?=><“”–+\'\]\[%_~#])'.format(specials))
    re_end = re.compile('([,.\-"!:\)\(;/—«»*?=><“”–+\'\]\[%_~#])(\S)'.format(specials))

    with open(ALL_FOR_BPE_FILE) as f, open(TMP_FILE, 'w') as wf:
        wf.write(' '.join(['?#!' + s for s in specials]) + '\n')
        for line in f:
            line = re_begin.sub(r'\1 \2', line)
            line = re_end.sub(r'\1 \2', line)
            wf.write(line)


if True:
    print('Train BPE model')
    yttm.BPE.train(
        data=TMP_FILE,
        vocab_size=50000,
        model=BPE_FILE,
        n_threads=10,
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

