# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:17:18 2018

@author: gsoun
"""

x = {"a":1,"b":2}
def fun():
    x["a"] = 3 
    print(x)
    return None

print(x)
fun()
print(x)