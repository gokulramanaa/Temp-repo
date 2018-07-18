# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 12:41:39 2018

@author: gsoun
"""

import numpy as np
import nltk
import pandas as pd
from variables import cols, d
from dataloader import test_data as tempor
from preorganizer import changedf
import _pickle
#rejli = {key:[] for key in cols}
#rejrli ={key:[] for key in cols}
#test = {key:set() for key in cols}

def tmapval(a, i, lin, rejli, rejrli):
    u,inv = np.unique(a,return_inverse= True)
    tel = tuple(np.array([d[x] for x in u])[inv])
    if tel not in lin[str(i)]:
        rejli[str(i)].append(tel)
        rejrli[str(i)].append("".join(a[2:-2]))
    
        
def feature_mapping(temp, tedf,lin, total, mingram,cfd, Xpd):
    rejli = {key:[] for key in cols}
    rejrli ={key:[] for key in cols}
    test = {key:set() for key in cols}
    for i in cols:
#        print("bef",rejrli)
        tdf = pd.DataFrame(tedf[str(i)].map(str).apply(list))
        tdf[str(i)].apply(tmapval, args = (i,lin, rejli, rejrli))
        print("Column ",str(i), "is completed")
#        print("after",rejrli)
        if len(rejli[str(i)]) !=0:
            for j in rejli[str(i)]:
                tr = nltk.ngrams(j,mingram[str(i)])
                if len(list(tr)) ==0:
                    vi = 0
                    tem = rejrli[str(i)][rejli[str(i)].index(j)]
                    test[str(i)].add(str("".join(tem)))
                    continue
                else:
                    tr = nltk.ngrams(j,mingram[str(i)])
                    cpairs = (((w[:-1]), w[-1]) for w in tr)
                    co = 0
                    vi = 0
                    for k in list(cpairs):
                        try:
                            v = cfd[str(i)][k[0]][k[1]]
                        except:
                            v =0
                        if co == 0:
                            vi = v/total[str(i)]
                            co = 1
                        else:
                            vi *= v/total[str(i)]
                    if vi ==0:
                        tel = rejrli[str(i)][rejli[str(i)].index(j)]
                        test[str(i)].add(str("".join(tel)))
        Xpd.loc[list(temp[temp[str(i)].isin(list(rejrli[str(i)]))].index),str(i)] = 0.5
        Xpd.loc[list(temp[temp[str(i)].isin(list(test[str(i)]))].index),str(i)] = 1
    return Xpd



def testmode(temp = tempor, lin = None,cfd = None,total=None, mingram=None, mode = "train"):
    if (mode != "feedback"):
        (lin,cfd,total,mingram) = _pickle.load(open("save.p", "rb"))
    tedf = changedf(temp)
    Xpd = pd.DataFrame(np.zeros(temp.shape), columns=temp.columns)
#    print("Xpd", Xpd.shape)
#    print(len(lin['a0']))
#    print(len(lin['a1']))
#    print(len(cfd['a0']))
#    print(len(cfd['a1']))
    Xpd = feature_mapping(temp, tedf, lin, total, mingram,cfd, Xpd)
    Xpd['sum'] = Xpd.sum(axis=1)
#    print(Xpd.head(25).tail(10))
    Rejectedpd = pd.DataFrame()
    AcceptedPd = pd.DataFrame()
    Rejectedpd = temp[Xpd['sum']>=2]
    Rejectedpd = Rejectedpd.reset_index(drop = True)
    AcceptedPd = temp[~(Xpd['sum']>=2)]
    print("=====SUMMARY=====")
    print("===Accepted table available in AcceptedPD===")
    print(AcceptedPd.shape[0],"rows are accepted out of", temp.shape[0])
    print("===Rejected table available in RejectedPD===")
    print(Rejectedpd.shape[0],"rows are rejected out of", temp.shape[0])
#    Rejectedpd.to_csv("C:/Users/gsoun/LogCorruptionFinder/Rejected.csv")
    return (Rejectedpd,AcceptedPd)
