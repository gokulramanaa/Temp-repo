# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:41:34 2018

@author: gsoun
"""
from datetime import datetime
startTime = datetime.now()
#from __future__ import generator_stop
import numpy as np
#import random
import nltk, string
#from nltk.util import ngrams
import pandas as pd
#from nltk.probability import *
#import string
#import copy
from sklearn.utils import shuffle

# li = ['timestamp', 'description','limit6','mailid','float']
# temp = pd.read_csv("./dataset.csv")
temp = pd.read_csv("C:/Users/gokul/Downloads/dst.csv", 
                            header=None, low_memory=False)

temp.columns = temp.columns.astype(str)
temp = shuffle(temp)
temp = temp.fillna("")
temp.to_csv("./input.csv")
tempn = pd.DataFrame()
for i in temp.columns:
    tempn[str(i)] = '*' + temp[str(i)].map(str) + '*'
le80 = int(0.8 * len(tempn))
npdf = tempn[:le80]
tedf = tempn[le80:]


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

d = map_parameter_init()
vi = dict()
cfd = dict()
mingram = dict()
total = dict()
cols = temp.columns
lin = {key:set() for key in cols}

li = ['0']
rejli = {key:[] for key in cols}
rejrli ={key:[] for key in cols}
rejin = {key:set() for key in cols}
indi = {key:[] for key in cols}
rejpd = pd.DataFrame(columns=temp.columns, index = range(300)) #.reindex_like(temp)

startTime = datetime.now()
def mapval(a, i):
#    print(a)
    u,inv = np.unique(a,return_inverse= True)
#    print(u)
    te = np.array([d[x] for x in u])[inv]
#    print(te)
    _,lind = np.unique(te, return_index=True)
    va = tuple(te[np.sort(lind)])
#    print(va)
#    print(te)
    lin[str(i)].add(va)

def trainmode():
    for i in cols:
        #distribution counting
        tokd = pd.DataFrame(npdf[str(i)].map(str).apply(list))
        tokd[str(i)].apply(mapval,args = (i,))

        ##Language model implementation
        toke = list(npdf[str(i)].str.cat(sep='\n'))
#        minv = npdf[str(i)].map(len).min()
        mingram[str(i)] = 3
        u,inv = np.unique(toke,return_inverse = True)
        te = np.array([d[x] for x in u])[inv].reshape(len(toke))
        total[str(i)] = len(te)
        bigr = nltk.ngrams(te,mingram[str(i)])
        condition_pairs = (((w[:-1]), w[-1]) for w in bigr)
        cfd[str(i)] = nltk.ConditionalFreqDist(condition_pairs)
        print(total[str(i)])
    print(cfd)
trainmode()
print(datetime.now() - startTime)


#run on actual data
startTime = datetime.now()
def tmapval(a, i):
    u,inv = np.unique(a,return_inverse= True)
    te = np.array([d[x] for x in u])[inv]
#    te = tuple(np.array([d[x] for x in u])[inv])
    _,lind = np.unique(te, return_index=True)
    te = tuple(te[np.sort(lind)])
    if te not in lin[str(i)]:
        try:
            rejin[str(i)].update(tempn[indi[str(i)].get_loc("".join(a))].index)
        except KeyError:
            rejin[str(i)].add(indi[str(i)].get_loc("".join(a)))
        rejli[str(i)].append(te)
        rejrli[str(i)].append(a)
        
def feature_mapping():
    for i in cols:
        ind = 0
        tdf = pd.DataFrame(tedf[str(i)].map(str).apply(list))
        indi[str(i)] = pd.Index(tempn[str(i)])
        tdf[str(i)].apply(tmapval, args = (i,))
        print("Number of rejected items in",str(i),"is", len(rejli[str(i)]),"\n")
        if len(rejli[str(i)]) !=0:
            for j in rejli[str(i)]:
                tr = nltk.ngrams(j,mingram[str(i)])
                if len(list(tr)) ==0:
                    vi = 0
                    tem = rejrli[str(i)][rejli[str(i)].index(j)]
                    rejpd.at[ind, str(i)] = str("".join(tem[1:-1]))
                    ind+=1
                    continue
                else:
                    tr = nltk.ngrams(j,mingram[str(i)])
                    cpairs = (((w[:-1]), w[-1]) for w in tr)
                    co = 0
                    vi = 0
                    for k in list(cpairs):
                        v = cfd[str(i)][k[0]][k[1]]
                        if co == 0:
                            vi = v/total[str(i)]
                            co = 1
                        else:
                            vi *= v/total[str(i)]
                    if vi ==0:
                        tel = rejrli[str(i)][rejli[str(i)].index(j)]
                        rejpd.at[ind, str(i)] = str("".join(tel[1:-1]))
                        ind+=1
#                    elif vi!=0:
#                        pass
#                         print("Accepted after language mode:","".join(rejrli[str(i)][rejli[str(i)].index(j)]))

x = feature_mapping()
print(datetime.now() - startTime)