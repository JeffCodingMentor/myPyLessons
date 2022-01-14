# -*- coding: utf-8 -*-
"""
a215. 明明愛數數
AC (25ms, 3.3MB)
2021-09-15 12:30
"""

while True:
    try:
        n, m = map(int, input().split())
        i=1
        s=n;
        while(s<=m):
            s+=(n+i)
            i+=1
        print(i)
    except:
        break