#! /usr/bin/env python3

def std_dev(list_num):
    """
    Returns the standard deviation of a list of numbers

        Parameters: 
            list_num (list): A list of positive integers
            
        Returns:
            A float, the standard deviation
    """

    # Calculate the mean of the numbers
    mean = sum(list_num)/len(list_num)

    # Initialise a variable to hold the sum of the squared distance to the mean
    sum_sqrd_dist = 0
    
    # Iterate over the numbers
    for num in list_num:
        # Subtract the mean from the number and square the result
        sqrd_dist = (num - mean)**2
        # Add the number to the sum of the squared distances 
        sum_sqrd_dist = sum_sqrd_dist + sqrd_dist

    # return the square root of the sum of squared distances divided by the length of the list
    return  (sum_sqrd_dist/len(list_num))**(1/2)

"""# Tests

print (std_dev([1,2,3,4,5,6,7,8,9]))
print (std_dev([11,21,31,41,51,61,71,81,91]))
print (std_dev([10,20,30,40,50,60,70,80,90]))
print (std_dev([1,5,15,30,50,75,105]))"""