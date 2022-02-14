# -*- coding: utf-8 -*-
"""
http://www.math.sjsu.edu/~foster/dictionary.txt
learned from https://stackoverflow.com/questions/4456446/dictionary-text-file

@author: JCM
"""
def getdict():
    dictionary = []
    with open("dictionary.txt") as f:
        word = f.readline()
        while word!="":
            if len(word)==6:   #there is a '\n' behind
                dictionary.append(word[0:5])
            word = f.readline()
    return dictionary

if __name__ == "__main__":
    dictionary = getdict()
    print(len(dictionary))
    #print(dict)
    
    str1 = "allwords=['"
    str1+= "','".join(dictionary)
    str1+= "']"
    
    with open("allwords.py", "w") as f:
        f.write(str1)
    

