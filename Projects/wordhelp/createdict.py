# -*- coding: utf-8 -*-
"""
http://www.math.sjsu.edu/~foster/dictionary.txt
learned from https://stackoverflow.com/questions/4456446/dictionary-text-file

@author: JCM
"""
def getdict():
    dict = []
    with open("dictionary.txt") as f:
        word = f.readline()
        while word!="":
            if len(word)==6:   #there is a '\n' behind
                dict.append(word[0:5])
            word = f.readline()
    return dict
    
    

if __name__ == "__main__":
    dict = getdict()
    print(len(dict))
    #print(dict)
    
    str1 = "allwords=["
    for word in dict:
        str1 += "'"+word+"',"
    str1 = str1[:-1]+"]"
    
    with open("allwords.py", "w") as f:
        f.write(str1)
    