# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n,m,k=map(int, input().split())

devils=[]
bombs=set()
for i in range(k):
    devil=[int(x) for x in input().split()]
    devils.append(devil)


while len(devils)!=0:
    for devil in devils[::-1]:
        bomb = (devil[0],devil[1])
        bombs.add(bomb)
        devil[0] += devil[2]
        devil[1] += devil[3]
        if devil[0]<0 or devil[0]>=n or devil[1]<0 or devil[1]>=m:
            devils.remove(devil)
    # print("move",devils)
    
    explode=set()
    if len(bombs)!=0:
        for devil in devils[::-1]:
            pos = (devil[0],devil[1])
            if pos in bombs:
                devils.remove(devil)
                explode.add(pos)

    bombs = bombs - explode
    
    # print("bombs", bombs)
    # print("survive", devils)
    
print(len(bombs))