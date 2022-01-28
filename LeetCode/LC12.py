# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 16:13:03 2021

@author: ManaTsao
"""

num = 1984

d1 = num//1000
d2 = (num//100)%10
d3 = (num//10)%10
d4 = num%10

# print(d1, d2, d3, d4)
res = ""

if d1>0:
    res += 'M'*d1

if d2>0:
    if d2==9:
        res += 'CM'
    elif d2==4:
        res += 'CD'
    else:
        if d2>=5:
            res += 'D'
            d2-=5
        res += 'C'*d2
        
if d3>0:
    if d3==9:
        res += 'XC'
    elif d3==4:
        res += 'XL'
    else:
        if d3>=5:
            res += 'L'
            d3-=5
        res += 'X'*d3

if d4>0:
    if d4==9:
        res += 'IX'
    elif d4==4:
        res += 'IV'
    else:
        if d4>=5:
            res += 'V'
            d4-=5

        res += 'I'*d4
print(res)
# return res
        