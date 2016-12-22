def nfruits(fruit, fruits_eaten):
    """
    fruit is a dictionary with the type of fruit as a key, and the amount as the value.
    fruits_eaten is a string
    returns the highest value after the fruit has been eaten and/or bought
    """
    
    count = 0
    for char in fruits_eaten:
        count += 1                               #keeps track of how many fruits eaten
        for key in fruit:
            if key == char:
                fruit[key] -= 1                  # eats fruit
            elif count != len(fruits_eaten):    # only buy fruit if it isn't the last fruit eaten
                fruit[key] += 1                  # buys fruit
    return max(fruit.values())