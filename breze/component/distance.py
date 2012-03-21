# -*- coding: utf-8 -*-


import theano.tensor as T

from norm import l1, l2


def cross_entropy(X, Y, axis=None):
    return -(X * T.log(Y)).sum(axis=axis)


def bernoulli_cross_entropy(X, Y, axis=None):
    return -(X * T.log(Y) + (1 - X) * T.log(1 - Y)).sum(axis=axis)


def squared(X, Y, axis=None):
    diff = X - Y
    return l2(diff, axis=axis)


def absolute(X, Y, axis=None):
    diff = X - Y
    return l1(diff, axis=axis)


def bernoulli_KL(X, Y):
    """
    Kullback-Leibler divergence between two
    bernoulli random variables _X_ and _Y_.
    """
    return (X*T.log(X/Y) + (1-X)*T.log((1-X)/(1-Y))).sum()


def entropy(X, axis=None):
    return -(X*T.log(X)).sum(axis=axis)
    
