# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:36:03 2018

@author: gsoun
"""
from datetime import datetime
from trainModel import trainmode
#from test import testmode

def main():
    print("Training takes place..")
    startTime = datetime.now()
    trainmode()
#    print(cfd['a0'][('*', '*')]['*'])
    print(datetime.now() - startTime)
    print("Training completed and testing takes place...")
    startTime = datetime.now()
#    Rejecte = testmode()
    print(datetime.now() - startTime)
#    return Rejecte


if __name__ == "__main__":
    main()
    
    
#import _pickle
#lin, cfd, to, mi = _pickle.load(open("save.p", "rb"))
##print(len(lin['a0']))
##print(len(lin['a1']))
##print(len(cfd['a0']))
##print(len(cfd['a1']))