# -*- coding: utf-8 -*-
'''
Zerojudge a121: 質數又來囉
AC (6.8s, 3.4MB) 	
2021-12-08 18:47

https://magiclen.org/prime-number/

1 100000000
5761455
'''
def isprime(n):
    if n==2 or n==3 or n==5:
        return True
    elif n>5:
        if n%5==0:
            return False
        
        m = n%6
        if m!=1 and m!=5:
            return False
        
        for i in range(5, int(n**0.5)+1, 6):
            if n%i==0 or n%(i+2)==0:
                return False
        return True
    else:
        return False
        

def countprime(begin, end):
    global count
    for i in range(begin, end+1):
        if isprime(i)==True:
            #print(i)
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