# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:50:24 2018

@author: Owner
"""

#! python3
# bulletPointAdder.py - Adds Wikipedia bulets point to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes
    lines[i] = '* ' + lines[i] #add star to each string
text = '\n'.join(lines)

pyperclip.copy(text)

