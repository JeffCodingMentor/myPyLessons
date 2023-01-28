# -*- coding: utf-8 -*-
"""
Created on Sun May 29 11:13:10 2022

@author: jcfan
"""

n, m, k = map(int, input().split())

players = [i for i in range(1, n+1)]

# print(players)
bomb=0
for i in range(k):
    bomb=bomb+m-1
    bomb%=len(players)
    # print(bomb, players[bomb])
    players.pop(bomb)                #AC 2.1s
    # players.remove(players[bomb])  #TLE
    # print(players)
    
bomb%=len(players)
print(players[bomb])