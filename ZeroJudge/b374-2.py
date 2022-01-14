# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:26:41 2021

@author: ManaTsao
"""

# n=12
# data_s=['2', '4', '2', '3', '2', '5', '3', '7', '2', '3', '4', '3']

n = input()
data_s = input().split()

data = list(map(int, data_s))
data_key = sorted(list(set(data)))
#print(data_key)
dict_c={}

max = 0
keylist = []

for d in data_key:
    c = data.count(d)
    dict_c[d]=c
    if c==max:
        keylist.append(d)
    elif c>max:
        keylist.clear()
        keylist.append(d)
        max=c

# print(max)
# print(dict_c)
# print(keylist)

for k in keylist:
    print("%d %d" % (k,dict_c[k]))
