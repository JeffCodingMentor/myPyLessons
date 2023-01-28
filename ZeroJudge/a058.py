answer = [0,0,0]
n = int(input())

for i in range(n):
    a = int(input())
    answer[a%3]+=1

print(*answer)