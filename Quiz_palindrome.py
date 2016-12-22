# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 16:21:56 2016

@author: Mark
"""

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    
    
    for ind, entry in enumerate(L):
        if f(entry) == False:
            L[ind] = False
    L[:] = (value for value in L if value != False)
        
    return len(L)


def f(s):
    return 'c' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L