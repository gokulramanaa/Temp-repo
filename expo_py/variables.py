# -*- coding: utf-8 -*-

#import pandas as pd
#import numpy as np
from map_initiator import map_parameter_init
from dataloader import temp

#global temp, tempn, d, tedf, npdf, cols, lin, mingram, cfd, total
#global rejli, rejrli, rejin, Xpd, test, Rejectedpd, train_data, test_data

#mapping character and numbers to c and n repectively and initiating training variables
d = map_parameter_init()
cfd = dict()
mingram = dict()
total = dict()
cols = temp.columns
lin = {key:set() for key in cols}


#initiating test variables
rejli = {key:[] for key in cols}
rejrli ={key:[] for key in cols}
rejin = {key:set() for key in cols}
test = {key:set() for key in cols}



