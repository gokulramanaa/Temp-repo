# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:41:34 2018

@author: gsoun
"""

from __future__ import generator_stop
import numpy as np
import random
import nltk, re, string, collections
from nltk.util import ngrams
import pandas as pd
from nltk.probability import *
import string
import copy
from sklearn.utils import shuffle

# li = ['timestamp', 'description','limit6','mailid','float']
# temp = pd.read_csv("./dataset.csv")
temp = pd.read_csv("C:/Users/gsoun/Downloads/Temp-repo-master/reld.csv", 
                   delimiter='|', header=None, low_memory=False)
temp.columns = temp.columns.astype(str)
temp = temp.fillna("")
temp.to_csv("./input.csv")
tempn = pd.DataFrame()
for i in temp.columns:
    tempn[str(i)] = '*' + temp[str(i)].map(str) + '*'
le80 = int(0.8 * len(tempn))
npdf = copy.deepcopy(tempn[:le80])
tedf = copy.deepcopy(tempn[le80:])



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
lin = {key:[] for key in cols}
rejli = {key:[] for key in cols}
rejrli ={key:[] for key in cols}
rejpd = pd.DataFrame(columns=temp.columns, index = range(300)) #.reindex_like(temp)



def mapval(x, i):
    a = np.array(x)
    _,idx = np.unique(a,return_index= True)
    u = a[[np.sort(idx)]]
    te = tuple(np.array([d[x] for x in u]))
    lin[str(i)].append(te)

def trainmode():
    for i in cols:
        #distribution counting
        tokd = pd.DataFrame(npdf[str(i)].map(str).apply(list))
        val = tokd[str(i)].apply(mapval,args = (i,))
        vi[str(i)] = collections.Counter(lin[str(i)])

        ##Language model implementation
        toke = list(npdf[str(i)].str.cat(sep='\n'))
        minv = npdf[str(i)].map(len).min()
        mingram[str(i)] = minv
        u,inv = np.unique(toke,return_inverse = True)
        te = np.array([d[x] for x in u])[inv].reshape(len(toke))
        total[str(i)] = len(te)
        bigr = nltk.ngrams(te,mingram[str(i)])
        condition_pairs = (((w[:-1]), w[-1]) for w in bigr)
        cfd[str(i)] = nltk.ConditionalFreqDist(condition_pairs)
        print(total[str(i)])
    print(cfd)


#run on actual data
def tmapval(x, va,i):
    a = np.array(x)
    _,idx = np.unique(a,return_index= True)
    u = a[[np.sort(idx)]]
    te = tuple(np.array([d[x] for x in u]))
    try:
        tel = vi[str(i)].get(te)/va
    except:
        rejli[str(i)].append(te)
        rejrli[str(i)].append(a)
        
def feature_mapping():
    count = 0
    for i in cols:
        ind = 0
        tdf = pd.DataFrame(tedf[str(i)].map(str).apply(list))
        count = len(tdf.index)
        tempa = tdf[str(i)].apply(tmapval, args = (count,i))
        print("Number of rejected items in",str(i),"is", len(rejli[str(i)]),"\n")
        if rejli[str(i)] !=[]:
            for j in rejli[str(i)]:
                tr = nltk.ngrams(j,mingram[str(i)])
                if list(tr) == []:
                    vi = 0
                    tem = copy.deepcopy(rejrli[str(i)][rejli[str(i)].index(j)])
                    tem.pop(0)
                    tem.pop(-1)
                    rejpd.at[ind, str(i)] = str("".join(tem))
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
                        tel = copy.deepcopy(rejrli[str(i)][rejli[str(i)].index(j)])
                        tel.pop(0)
                        tel.pop(-1)
                        rejpd.at[ind, str(i)] = str("".join(tel))
                        ind+=1
                    elif vi!=0:
                        pass
#                         print("Accepted after language mode:","".join(rejrli[str(i)][rejli[str(i)].index(j)]))
                
trainmode()
x = feature_mapping()