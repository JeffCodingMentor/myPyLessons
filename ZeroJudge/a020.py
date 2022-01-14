# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:27:49 2021

@author: ManaTsao
"""

#id = "T112663836"
#id = "S154287863"

letters = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17,\
           'I':34, 'J':18, 'K':19, 'L':20, 'M':21, 'N':22, 'O':35, 'P':23,\
           'Q':24, 'R':25, 'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30,\
           'Y':31, 'Z':33}

id = input()
n = letters[id[0]]
sum = n//10 + (n%10)*9

for i in range(1,9):
    sum += (9-i)*int(id[i])

sum += int(id[9])

if sum%10 == 0:
    print("real")
else:
    print("fake")