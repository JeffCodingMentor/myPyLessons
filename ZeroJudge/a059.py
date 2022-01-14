# -*- coding: utf-8 -*-
'''
Zerojudge a059: 完全平方和
AC (16ms, 3.3MB)
2021-12-08 16:09
'''
T = int(input())
t = 0
SumofSqrNs = []

while t<T :
    
    a = int(input())
    b = int(input())
    SumofSqrN = 0
    
    for n in range(a, b+1):
        if n == (int(n**0.5))**2:
            SumofSqrN += n 
    SumofSqrNs.append(SumofSqrN)
    t+=1

t = 0
while t<T :
    print(f"Case {t+1}: {SumofSqrNs[t]}")
    t+=1