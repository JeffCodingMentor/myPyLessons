# -*- coding: utf-8 -*-
"""
createpddict.py
    read from dictionary2.txt to create allwords.py by using pandas
    dictionary2.txt is generated from:
    http://app.aspell.net/create?max_size=60&spelling=US&max_variant=0&diacritic=strip&special=hacker&special=roman-numerals&download=wordlist&encoding=utf-8&format=inline

@author: JCM
"""

import pandas as pd

url = "dictionary2.txt"

df = pd.read_csv(url, header=None, names=["word"])      #Giving a column name "word"
df = df.drop(df[df['word'].str.len() != 5].index)       #Drop words w/ length not equal to 5
df = df.drop(df[df['word'].str.find("'") != -1].index)  #Drop words w/ ' in it
df = df.apply(lambda x: x.astype(str).str.lower())      #Make all words to lower case

dictionary = df['word'].tolist()                        #Convert to list
# print(text_data)

str1 = "allwords=['"
str1+= "','".join(dictionary)
str1+= "']"
print(str1)
print(len(dictionary))

with open("allwords.py", "w") as f:
    f.write(str1)