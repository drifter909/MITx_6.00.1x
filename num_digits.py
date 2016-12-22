def ndigits(x):
    ''' 
    Takes an input of an int or a float, and returns the number of digits by 
    making a recursive call
    '''
    if abs(x) < 10:                  #base case
        return 1         
    else:
        return 1 + ndigits(x/10)     #recursive call

print ndigits(10050)