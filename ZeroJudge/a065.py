# -*- coding: utf-8 -*-
"""
a065 密碼問題
Created on Thu Sep  9 09:51:31 2021
@author: Jeff
"""
while True:
    try:
        s = input()
        for i in range(1,len(s)):
            print(abs(ord(s[i])-ord(s[i-1])),end="")
    except:
        break
    else:
        print()