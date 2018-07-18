# -*- coding: utf-8 -*-

import pandas as pd

def changedf(df):
    new_df = pd.DataFrame()
    for i in df.columns:
        new_df[str(i)] = '* ' + df[str(i)].map(str) + ' *'
    return new_df
