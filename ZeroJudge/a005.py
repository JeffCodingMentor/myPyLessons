# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:14:06 2021

@author: ManaTsao
"""

n=int(input())
i=0

while(i<n):
    data0=input().split()
    data=list(map(int,data0))
    data.append(0)
    # print(data)
    
    if(data[1]-data[0]==data[2]-data[1]):
        data[4]=data[3]+(data[3]-data[2])
        
    if(data[1]*data[3]==data[2]*data[2]):
        data[4]=int(data[3]*(data[3]/data[2]))
        
    for j in range(5):
        print(data[j], end=" ")
    
    i+=1
    print()