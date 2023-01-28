# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n,m,k=map(int, input().split())

devils=[]
bombs=[]
for i in range(k):
    devil=[int(x) for x in input().split()]
    devils.append(devil)


while len(devils)!=0:
    for devil in devils[::-1]:
        bomb = (devil[0],devil[1])
        if bomb not in bombs:
            bombs.append(bomb)
        devil[0] += devil[2]
        devil[1] += devil[3]
        if devil[0]<0 or devil[0]>=n or devil[1]<0 or devil[1]>=m:
            devils.remove(devil)
    # print("move",devils)
    
    for bomb in bombs[::-1]:
        explode=False
        for devil in devils[::-1]:
            #if bomb[0]==devil[0] and bomb[1]==devil[1]:
            if bomb == (devil[0],devil[1]):
                devils.remove(devil)
                explode=True
        if explode:
            bombs.remove(bomb)
    
    # print("bombs", bombs)
    # print("survive", devils)
    
print(len(bombs))