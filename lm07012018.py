# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:41:34 2018

@author: gsoun
"""
from datetime import datetime
startTime = datetime.now()
#from __future__ import generator_stop
#import random
#from nltk.probability import *
#import string
#import copy
#from nltk.util import ngrams
import numpy as np
import nltk, string
import pandas as pd
from sklearn.utils import shuffle

# li = ['timestamp', 'description','limit6','mailid','float']
# temp = pd.read_csv("./dataset.csv")
temp = pd.read_csv("C:/Users/gsoun/Downloads/Temp-repo-master/reld.csv", 
                   delimiter='|', header=None, low_memory=False)

df = pd.read_csv("C:/Users/gsoun/Book1.csv")

temp.columns = temp.columns.astype(str)
temp = shuffle(temp)
temp = temp.fillna("")
temp.to_csv("./input.csv")
tempn = pd.DataFrame()
for i in temp.columns:
    tempn[str(i)] = '* ' + temp[str(i)].map(str) + ' *'
le80 = int(0.8 * len(tempn))
npdf = tempn[:le80]
tedf = tempn[le80:]

# =============================================================================
# d 
#  '|': '|',
#  '9': 'n',
#  'a': 'c',
# =============================================================================
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

# =============================================================================
# VARIABLE INITIALIZATION
# =============================================================================
d = map_parameter_init()
vi = dict()
cfd = dict()
mingram = dict()
total = dict()
cols = temp.columns
lin = {key:set() for key in cols}


rejli = {key:[] for key in cols}
rejrli ={key:[] for key in cols}
rejin = {key:set() for key in cols}
indi = {key:[] for key in cols}
#rejpd = pd.DataFrame(columns=temp.columns, index = range(300)) #.reindex_like(temp)
Xpd = pd.DataFrame(np.zeros(temp.shape), columns=tedf.columns)
test = {key:set() for key in cols}


startTime = datetime.now()
def mapval(a, i):
    u,inv = np.unique(a,return_inverse= True)
    tel = tuple(np.array([d[x] for x in u])[inv])
    lin[str(i)].add(tel)

def trainmode():
    for i in cols:
        #distribution counting
        val = pd.DataFrame(np.unique(npdf[str(i)]))
        tokd = pd.DataFrame(val[0].map(str).apply(list))
        tokd[0].apply(mapval,args = (i,))

        ##Language model implementation
        toke = list(val[0].str.cat(sep='\n'))
        mingram[str(i)] = 3
        u,inv = np.unique(toke,return_inverse = True)
        te = np.array([d[x] for x in u])[inv].reshape(len(toke))
        total[str(i)] = len(te)
        bigr = nltk.ngrams(te,mingram[str(i)])
        condition_pairs = (((w[:-1]), w[-1]) for w in bigr)
        cfd[str(i)] = nltk.ConditionalFreqDist(condition_pairs)
        print("Column ",str(i), "is completed")
    print(cfd)
    
print("Training takes place..")
trainmode()
print(datetime.now() - startTime)
print("Training completed and testing takes place in testing data")


startTime = datetime.now()
def tmapval(a, i):
    u,inv = np.unique(a,return_inverse= True)
    tel = tuple(np.array([d[x] for x in u])[inv])
    if tel not in lin[str(i)]:
        rejli[str(i)].append(tel)
        rejrli[str(i)].append("".join(a[2:-2]))
        
def feature_mapping():
    for i in cols:
#        ind = 0
        tdf = pd.DataFrame(tedf[str(i)].map(str).apply(list))
        indi[str(i)] = pd.Index(tempn[str(i)])
        tdf[str(i)].apply(tmapval, args = (i,))
        print("Column ",str(i), "is completed")
        if len(rejli[str(i)]) !=0:
            for j in rejli[str(i)]:
                tr = nltk.ngrams(j,mingram[str(i)])
                if len(list(tr)) ==0:
                    vi = 0
                    tem = rejrli[str(i)][rejli[str(i)].index(j)]
#                     rejpd.at[ind, str(i)] = str("".join(tem))
#                     ind+=1
                    test[str(i)].add(str("".join(tem)))
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
#                         rejpd.at[ind, str(i)] = str("".join(tel))
#                         ind+=1
                        test[str(i)].add(str("".join(tel)))
        Xpd.loc[list(temp[temp[str(i)].isin(list(rejrli[str(i)]))].index),str(i)] = 0.5
        Xpd.loc[list(temp[temp[str(i)].isin(list(test[str(i)]))].index),str(i)] = 1
    
x = feature_mapping()
Xpd['sum'] = Xpd.sum(axis=1)
Rejectedpd = temp[Xpd['sum']>=2]
AcceptedPd = temp[~(Xpd['sum']>=2)]
print("=====SUMMARY=====")
print("===Accepted table available in AcceptedPD===")
print(AcceptedPd.shape[0],"rows are accepted out of", temp.shape[0])
print("===Rejected table available in RejectedPD===")
print(Rejectedpd.shape[0],"rows are rejected out of", temp.shape[0])
print(datetime.now() - startTime)