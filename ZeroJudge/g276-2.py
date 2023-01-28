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
    
    temp = []
    indx = []
    if len(bombs)!=0:
        for devil in devils:
            pos = (devil[0],devil[1])
            if pos in bombs:
                i = bombs.index(pos)
                if i not in indx:
                    indx.append(i)
            else:
                temp.append(devil)
    devils, temp = temp, devils
    for i in sorted(indx, reverse=True):
        bombs.pop(i)

    print("bombs", bombs)
    print("survive", devils)
    
print(len(bombs))