# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:26:41 2021

@author: ManaTsao
"""

#n=12
#data_s=['2', '4', '2', '3', '2', '5', '3', '7', '2', '3', '4', '3']

n = input()
data_s = input().split()

data = list(map(int, data_s))
data_key = sorted(list(set(data)))
#print(data_key)
dict_c={}

for d in data_key:
    c = data.count(d)
    dict_c[d]=c
    
#print(dict_c)

m = max(dict_c.values())
for k, v in dict_c.items():
    if v==m:
        print("%d %d" % (k,v))