# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:49:02 2018

@author: Owner
"""

grid = [['.', '.', '.', '.', '.', '.'], ['.', 'O', 'O', '.', '.', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['O', 'O', 'O', 'O', 'O', '.'], ['.', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['.', 'O', 'O', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]
def picturegrid(z):
    x = 0
    y = 0
    while y < len(z[0]):
        while x < len(z):
            print(z[x][y], end = "")
            x += 1
            if x == len(z):
                print()
        y += 1
        x = 0    
picturegrid(grid)