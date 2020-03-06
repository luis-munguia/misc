# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:35:05 2018

@author: Owner
"""

import random

messages = ['It is certain', 'It is decidecly so',
            'Yes definitely', 'Reply hazy try again',
            'Ask Again Later', 'Concentrate and ask again']
print(messages[random.randint(0,len(messages)-1)])
