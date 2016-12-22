# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:10:18 2016
@author: Mark

This function takes 2 parameters (the number of sides
and the length of one side) for a regular polygon.  The function
returns the value of its area + perimeter squared rounded to 4
decimal places.
"""

import math
def polysum(n,s):
    area = (0.25*n*s*s) / math.tan(math.pi / n)
    perimeter = n*s
    
    return round(area + perimeter**2,4)