# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:16:12 2018

@author: Owner
"""

list1 = ["apple","orange","watermelon","grape","strawberry"]

def binary_search(x,y):
    """Binary search function, searches for item and gives the index"""
    
    for i in range(len(x)):
        if x[i] == y:
            return print("The item index",i)
        else:
            return -1
