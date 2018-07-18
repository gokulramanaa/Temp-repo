# -*- coding: utf-8 -*-

import string 

def map_parameter_init():
    d = {}
    pun = list(string.punctuation)
    num = list(string.digits)
    let = list(string.ascii_letters)
    for i in pun:
        d[i] = i
    for j in num:
        d[j] = 'n'
    for k in let:
        d[k] = 'c'
    d[' '] = ' '
    d['\n'] = '\n'
    d['\t'] = '\t'
    return d
