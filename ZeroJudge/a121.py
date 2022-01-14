# -*- coding: utf-8 -*-
'''
Zerojudge a121: 質數又來囉
TLE (9s) 	
2021-12-08 17:07

'''
prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
             101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
             211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
             307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
             401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
max_num = 500

def findprime(new_max):
    global max_num
    for i in range(max_num+1, new_max+1):
        is_prime=True
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime==True:
            prime_nums.append(i)
            
    max_num=new_max
    
while True:
    try:
        line = input()
        numbers = line.split(" ")
        begin, end = int(numbers[0]), int(numbers[1])
        
        if end > max_num:
            findprime(end)
        
        pnum_inrange = filter(lambda x: (begin<=x<=end), prime_nums)

        print(len(list(pnum_inrange)))
    except EOFError:
        #print("EOF") #CTRL+D (for *nix) or CTRL+Z (for Windows) 
        break