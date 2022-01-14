# -*- coding: utf-8 -*-
'''
Zerojudge a121: 質數又來囉
TLE (9s) 	
2021-12-08 17:22

https://magiclen.org/prime-number/
'''
def isprime(n):
    if n==2 or n==3:
        return True
    elif n>4:
        # if n%5==0:
        #     return False
        
        m = n%6
        if m!=1 and m!=5:
            return False
        
        for i in range(5, int(n**0.5), 6):
            if n%i==0 or n%(i+2)==0:
                return False
        return True
    else:
        return False
        

def countprime(begin, end):
    global count
    for i in range(begin, end+1):
        is_prime=True
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime==True:
            # print(i)
            count+=1
    
while True:
    try:
        line = input()
        numbers = line.split(" ")
        begin, end = int(numbers[0]), int(numbers[1])
        count = 0
        
        if begin==1:
            begin =2
        
        countprime(begin, end)

        print(count)
    except EOFError:
        #print("EOF") #CTRL+D (for *nix) or CTRL+Z (for Windows) 
        break