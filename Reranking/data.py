# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import os
import numpy as np
import torch


def get_batch(batch, word_vec, emb_dim=300):
    # sent in batch in decreasing order of lengths (bsize, max_len, word_dim)
    lengths = np.array([len(x) for x in batch])
    max_len = np.max(lengths)
    embed = np.zeros((max_len, len(batch), emb_dim))

    for i in range(len(batch)):
        for j in range(len(batch[i])):
            embed[j, i, :] = word_vec[batch[i][j]]

    return torch.from_numpy(embed).float(), lengths


def get_word_dict(sentences):
    # create vocab of words
    word_dict = {}
    for sent in sentences:
        for word in sent.split():
            if word not in word_dict:
                word_dict[word] = ''
    word_dict['<s>'] = ''
    word_dict['</s>'] = ''
    word_dict['<p>'] = ''
    return word_dict


def get_glove(word_dict, glove_path):
    # create word_vec with glove vectors
    word_vec = {}
    with open(glove_path) as f:
        for line in f:
            word, vec = line.split(' ', 1)
            if word in word_dict:
                word_vec[word] = np.array(list(map(float, vec.split())))
    print('Found {0}(/{1}) words with glove vectors'.format(
                len(word_vec), len(word_dict)))
    return word_vec


def build_vocab(sentences, glove_path):
    word_dict = get_word_dict(sentences)
    word_vec = get_glove(word_dict, glove_path)
    print('Vocab size : {0}'.format(len(word_vec)))
    return word_vec


def get_nli(data_path):
    s1 = {}
    s2 = {}
    target = {}

    dico_label = {'entailment': 0,  'neutral': 1, 'contradiction': 2}

    for data_type in ['train', 'dev', 'test']:
        s1[data_type], target[data_type] = {}, {}
    s1['train']['path'] = ##
    s1['dev']['path'] = ##
    s1['test']['path'] = ##
    target['train']['path'] = ##
    target['dev']['path'] = ##
    target['test']['path'] = ##
    s1['train']['sent'] = [line.rstrip() for line in open(s1['train']['path'], 'r')]
    s1['dev']['sent'] = [line.rstrip() for line in open(s1['dev']['path'], 'r')]
    s1['test']['sent'] = [line.rstrip() for line in open(s1['test']['path'], 'r')]
    target['train']['data'] = np.array([line.rstrip('\n').split() for line in open(target['train']['path'], 'r')])
    target['dev']['data'] = np.array([line.rstrip('\n').split() for line in open(target['dev']['path'], 'r')])
    target['test']['data'] = np.array([line.rstrip('\n').split() for line in open(target['test']['path'], 'r')])
    target['train']['data']=target['train']['data'].astype(np.float)
    target['dev']['data']=target['dev']['data'].astype(np.float)
    target['test']['data']=target['test']['data'].astype(np.float)
                
    assert len(s1['train']['sent'])  == len(target['train']['data'])
    assert len(s1['dev']['sent'])  == len(target['dev']['data'])

    print('** {0} DATA : Found {1} pairs of {2} sentences.'.format(data_type.upper(), len(s1['train']['sent']), data_type))
    print('** {0} DATA : Found {1} pairs of {2} sentences.'.format(data_type.upper(), len(s1['dev']['sent']), data_type))

    train = {'s1': s1['train']['sent'],
             'label': target['train']['data']}
    dev = {'s1': s1['dev']['sent'], 
           'label': target['dev']['data']}
    test={'s1': s1['test']['sent'], 
           'label': target['test']['data']}

    return train, dev, test
