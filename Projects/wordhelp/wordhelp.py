# -*- coding: utf-8 -*-
"""
wordhelp.py
    Wordle Helper

@author: JCM
"""

#import createdict
import allwords
import random

#candidates = createdict.getdict()  #use this if dictionary.txt is ever changed
candidates = allwords.allwords

for k in range(6):
    print(len(candidates))
    if len(candidates)==0:
        print("Something wrong")
        break
    
    guess = random.choice(candidates)
    print(guess)
    result = input("result: ")
    
    if result == "vvvvv":
        print("Congratulations")
        break
    
    temp_candidate = candidates[:]
    for check_word in candidates:
        remove = False
        for i in range(5):
            if result[i] == "x":
                if guess[i] in check_word:
                    remove = True
                    
            elif result[i] == "v":
                if guess[i] != check_word[i]:
                    remove = True
    
            else:
                if guess[i] not in check_word:
                    remove = True
                elif guess[i]==check_word[i]:
                    remove = True

            if remove == True:
                temp_candidate.remove(check_word)
                break
    
    candidates = temp_candidate
    if(len(candidates)<150): print(candidates)