# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:56:59 2016

@author: Mark
"""

low_bound = 0
high_bound = 100

print "Please think of a number between 0 and 100!"

while True:
    print "Is your secret number " + str((low_bound + high_bound) / 2)
    loc = raw_input("Enter 'h' to indicate the guess is too high.  "\
                    "Enter 'l' to indicate the guess is too low.  "\
                    "Enter 'c' to indicate I guessed correctly.")
    if loc == 'h':
        high_bound = (low_bound + high_bound) / 2
    elif loc == 'l':
        low_bound = (low_bound + high_bound) / 2
    elif loc == 'c':
        print "Game over.  Your secret number was: " + str((low_bound + high_bound) / 2)
        break
    else:
        print "Sorry, I did not understand your input."