# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 11:25:48 2016

@author: Mark
"""

def getSublists(L, n):
    for entry in L:
        if len(L) == n:
            return [L]
        return [L[:n]] + getSublists(L[1:],n)

def longestRun(L):
    for i in range(len(L),0,-1):
        sublists = getSublists(L,i)
        for entry in sublists:
            print entry
            if sorted(entry) == entry:
                return len(entry)
                
            
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
#L = [1,2,3,4,5]            

print longestRun(L)