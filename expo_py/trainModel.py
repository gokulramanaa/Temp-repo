# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from variables import cols, d
from dataloader import train_data
import nltk
import _pickle
from preorganizer import changedf

from variables import lin, cfd, total, mingram


def mapval(a, i):
    u,inv = np.unique(a,return_inverse= True)
    tel = tuple(np.array([d[x] for x in u])[inv])
    lin[str(i)].add(tel)
    
def trainmode(df = train_data, mode = "train"):
    npdf = changedf(df)
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
    if (mode == "feedback"):
        (lind,cfdd,totald,mingramd) = _pickle.load(open("save.p","rb"))
        linn = {key:set() for key in cols}
        cfdn = dict()
        for ij in cols:
            linn[str(ij)] = lind[str(ij)] | lin[str(ij)]
            cfdn[str(ij)] = {**dict(cfdd[str(ij)]),**dict(cfd[str(ij)])}
#            totaln[str(ij)] = {**dict(totald[str(ij)]), **dict(total[str(ij)])}
        tobestored = (linn,cfdn,totald, mingramd)
        return (linn,cfdn,totald, mingramd)
#        _pickle.dump(tobestored, open("save.p","wb"))
#        print(cfdn)
    elif (mode=="train"):
        tobestored = (lin,cfd,total,mingram)
        _pickle.dump(tobestored,open("save.p", "wb"))
        print(cfd)
        