# -*- coding: utf-8 -*-
"""
a216. 數數愛明明
AC (0.2s, 5.9MB)
2021-09-14 14:22
"""

flist = [0]*30001
glist = [0]*30001
flist[1]=1
glist[1]=1

while True:
    try:
        n=int(input())
        i=2
        while i<=n:
            if flist[i]==0:
                flist[i]=i*(i+1)//2
            if glist[i]==0:
                glist[i]=flist[i]+glist[i-1]
            i+=1
        print(flist[n], glist[n])
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