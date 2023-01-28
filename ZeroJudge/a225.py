"""
Zerojedge a225


"""
while True:
    try:
        res=[ [] for i in range(10)]

        N = int(input())
        nums = [int(x) for x in input().split()]
        for n in nums:
            m=n%10
            res[m].append(n)
            res[m].sort(reverse=True)

        for i in range(10):
            if res[i]!=0:
                for n in res[i]:
                    print(n, end=" ")
        print()
    except:
        break