# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:48:58 2022

@author: JCM
"""

# -*- coding: utf-8 -*-
"""
mergedict.py
    merge dictionary.txt and dictionary2.txt to create allwords.py by usign pandas

@author: JCM
"""

import pandas as pd

file1 = "dictionary.txt"
df1 = pd.read_csv(file1, header=None, names=["word"]) 
df1 = df1.drop(df1[df1['word'].str.len() != 5].index)
df1 = df1.apply(lambda x: x.astype(str).str.lower()) 

file2 = "dictionary2.txt"
df2 = pd.read_csv(file2, header=None, names=["word"])       #Giving a column name "word"
df2 = df2.drop(df2[df2['word'].str.len() != 5].index)       #Drop words w/ length not equal to 5
df2 = df2.drop(df2[df2['word'].str.find("'") != -1].index)  #Drop words w/ ' in it
df2 = df2.apply(lambda x: x.astype(str).str.lower())        #Make all words to lower case
df2.drop_duplicates(subset="word", keep='first', inplace=True)  #Remove redundant word in dictionary2

df = pd.merge(df1, df2, how="inner")                        #Merge 2 dataframes
dictionary = df['word'].tolist()                            #Convert to list

df_diff  =pd.concat([df2,df1,df1]).drop_duplicates(keep=False)
print(df_diff)

str1 = "allwords=['"
str1+= "','".join(dictionary)
str1+= "']"
#print(str1)
print(len(df1), len(df2))
print(len(dictionary))

with open("allwords.py", "w") as f:
    f.write(str1)