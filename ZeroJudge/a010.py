# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:50:33 2021

@author: ManaTsao
"""

prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
             101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
             211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
             307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
             401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

n=int(input())
i=0
ans={}

while n!=1:
    if n%prime_nums[i]!=0:
        i+=1
        continue

    while n%prime_nums[i]==0:
        ans[prime_nums[i]] = ans.get(prime_nums[i],0)+1
        n//=prime_nums[i]

    i+=1

if len(ans)==1:
    ans[1]=1

anskey = sorted(list(ans.keys()))

for i in range(len(anskey)):
    print(anskey[i], end='')
    if(ans[anskey[i]]>1): print('^'+str(anskey[i]), end='')
    if(i!=len(anskey)-1): print(" * ", end='')