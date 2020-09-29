# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:29:36 2020

@author: HARSHDA SABLE
"""


file=open("Desktop/sample.txt","rt")
data=file.read(100)
print(data)
occurrences=data.count("resolve")
words=data.split()


print("number of words in text file:",len(words))
print(" number of occurrences of word:",occurrences)