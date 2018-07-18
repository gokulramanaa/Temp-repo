# -*- coding: utf-8 -*-
import pandas as pd

temp = pd.read_csv("C:/Users/gsoun/Downloads/Temp-repo-master/reld.csv", 
               delimiter='|', header=None, low_memory=False)
temp.columns = temp.columns.map(lambda x: "a" + str(x))
temp = temp.fillna("")
#temp = temp.head(100000)
le80 = int(0.2 * len(temp))
test_data = temp[:le80]
train_data = temp[le80:]