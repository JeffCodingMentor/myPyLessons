# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:26:41 2021

@author: ManaTsao
"""

n=12
data_s=['2', '4', '2', '3', '2', '5', '3', '7', '2', '3', '4', '3']

# n = input()
# data_s = input().split()

data = list(map(int, data_s))
dict_c={}

for d in data:
    if d in dict_c:
        dict_c[d]+=1
    else:
        dict_c[d]=1
# print(dict_c)

m = max(dict_c.values())
for k, v in dict_c.items():
    if v==m:
        print("%d %d" % (k,v))