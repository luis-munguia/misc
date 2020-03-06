# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:11:29 2018

@author: Owner
"""

def commacode(anylist):
    i = 0
    while i < len(anylist)-1:
        print(anylist[i] + ", ", end = "")
        i += 1
    print("and " + anylist[-1] + ".")
    
spam = ['apples', 'bananas', 'tofu', 'cats', 'gorillas', 'space', 'dictionary']
commacode(spam)