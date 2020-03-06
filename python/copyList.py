# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:54:57 2018

@author: Owner
"""

def eggs(someParameter):
    someParameter.append('Hello')
    
spam = [1,2,3]
eggs(spam)
print(spam)