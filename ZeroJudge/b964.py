n = int(input())
s = sorted([int(x) for x in input().split()])
print(*s)

p = [x for x in s if x>=60]
f = [x for x in s if x<60]

if len(f)==0:
    print("best case")
else:
    print(f[-1])
    
if len(p)==0:
    print("worst case")
else:
    print(p[0])