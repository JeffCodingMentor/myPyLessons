# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:53:56 2021

"""

while True:
    try:
        data = []
        num = input()
        data0 = input().split()
        data = list(map(int, data0))
        data.sort()
        for i in data:
            print(i, end=" ")
        print()
    except:
        break