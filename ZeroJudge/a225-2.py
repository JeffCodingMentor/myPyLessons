from queue import PriorityQueue 

while True:

    try:
        pq = PriorityQueue()
        n=int(input())
        nums = [(int(x)%10, int(x)//-10, int(x)) for x in input().split()]

        for t in nums:
            pq.put(t)

        while pq.empty()==False:
            print(pq.get()[2],end=" ")

        print()
    except:
        break