n, k = map(int, input().split())
p = [int(x) for x in input().split()]
p.sort()
s = p[-1]-p[0]
dmax = s//k+1
dmin = 1

# print(n,k)
# print(p)
# print(s, dmax, dmin)

def cover(d):
    start = p[0]
    end = p[0]+d
    count = 1
    for i in range(len(p)):
        if p[i] <= end: continue
        count+=1
        if count > k: return False
        start = p[i]
        end = start + d
    return True

'''
for dmid in range(dmin, dmax+1):
    if cover(dmid):
        print(dmid)
        break
'''

while dmin<=dmax:
    dmid=(dmin+dmax)//2
    if cover(dmid): dmax=dmid
    else: dmin=dmid+1

    if dmin==dmax:
        print(dmin)
        break