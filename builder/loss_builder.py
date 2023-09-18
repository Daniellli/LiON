# -*- coding:utf-8 -*-

# @file: loss_builder.py 

import torch
from utils.lovasz_losses import lovasz_softmax


def build(wce=True, lovasz=True, num_class=20, ignore_label=0):

    loss_funs = torch.nn.CrossEntropyLoss(ignore_index = ignore_label)

    if wce and lovasz:
        return loss_funs, lovasz_softmax
    elif wce and not lovasz:
        return wce
    elif not wce and lovasz:
        return lovasz_softmax
    else:
        raise NotImplementedError

def build_ood(wce=True, lovasz=True, num_class=20, ignore_label=0, weight=1):

    weights = torch.ones(num_class+1).cuda()
    weights[-1] = weight
    loss_funs = torch.nn.CrossEntropyLoss(weight = weights, ignore_index = ignore_label)

    if wce and lovasz:
        return loss_funs, lovasz_softmax
    elif wce and not lovasz:
        return wce
    elif not wce and lovasz:
        return lovasz_softmax
    else:
        raise NotImplementedError
