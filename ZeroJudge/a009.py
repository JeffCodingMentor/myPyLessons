# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:44:31 2021

@author: ManaTsao
"""

s=input()
r=[]

for i in range(len(s)):
    m = chr(ord(s[i])-7)
    print(m, end='')