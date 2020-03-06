# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:29:43 2018

@author: Owner
"""

#! python 3
# pw.py An insecure password locker program.

PASSWORDS = {'email': '12345678', 'blog': 'abcdefg', 'luggage': '9238'}
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy accont password')
    sys.exit()
    
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboad.')
else:
    print('There is no account named ' + account)
