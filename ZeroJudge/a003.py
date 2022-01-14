# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:58:18 2021

"""

data_s = input().split()
M = int(data_s[0])
D = int(data_s[1])
R = (M*2+D)%3

if R==0:
    print("普通")
elif R==1:
    print("吉")
else:
    print("大吉")
