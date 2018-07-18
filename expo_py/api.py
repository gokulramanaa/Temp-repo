# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 08:28:53 2018

@author: gsoun
"""

#import pandas as pd
#import requests
from datetime import datetime
import json
from flask import Flask, request
#import json
from test import testmode
from trainModel import trainmode

app = Flask(__name__)
startTime = datetime.now()

@app.route("/test")
def hello_react():
    df['index'] = df.index
    d = [ dict([(colname, row[i]) 
        for i,colname in enumerate(df.columns)])for row in df.values]
    return json.dumps(d)


@app.route('/api/add_message/<uuid>', methods=['GET','POST'])
def add_message(uuid):
    content = request.get_json(force=True)
    dfd = df[content]
    linn,cfdn,totald, mingramd = trainmode(dfd, mode = "feedback")
#    print(len(linn['a0']))
#    print(linn['a1'])
#    print(len(linn['a1']))
#    print(len(cfdn['a0']))
#    print(len(cfdn['a1']))
    dfn,_ = testmode(df, linn,cfdn,totald, mingramd, mode = "feedback")
    print(dfn.shape)
    dfn['index'] = dfn.index
    d = [ dict([(colname, row[i]) 
        for i,colname in enumerate(dfn.columns)])for row in dfn.values]
    return json.dumps(d)
    
global df
df,af = testmode()
#print(df)
app.run(debug = False)