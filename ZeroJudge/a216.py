# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:18:59 2021

@author: ManaTsao
"""
flist = [0]*30001
glist = [0]*30001
flist[1]=1
glist[1]=1

def f(n):
    if flist[n]!=0:
        return flist[n]
    else:
        flist[n]=n+f(n-1)
        return flist[n]

def g(n):
    if glist[n]!=0:
        return glist[n]
    else:
        glist[n]=f(n)+g(n-1)
    return glist[n]

while True:
    try:
        n=int(input())
        if n>500:
            i=1
            while i<n//500:
                f(500*i)
                g(500*i)
                i+=1
        print(f(n), g(n))
    except:
        break

#RecursionError: maximum recursion depth exceeded in comparison
# n=27001
# if n>1000:
#     i=1
#     while i<n//1000:
#         f(1000*i)
#         g(1000*i)
#         i+=1
#         print(1000*i)
# print(f(n), g(n))            