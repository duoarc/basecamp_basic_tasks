#! /usr/bin/env python3


def sum_even_odd(list_of_num):
    """
    Returns a list of the sum of even positive integers and the sum of the negative integers.

        Parameters: 
            list_of_num (list): List of positive integers 

        Returns:
            list_sum (list): List of sum of even integers, odd integers [sum_even, sum_odd]
    """

    # Check if the list of integers has any negative numbers

    for num in list_of_num:
        if num < 0:
            return "Please provide positive numbers only and try again"
    
    # Handle Zeroes

    if 0 in list_of_num:
        return "Please provide positive numbers only and try again. Zero is not a positive number!"

    # Initialise variables to hold sum of even number and sum of odd numbers
    sum_even = 0
    sum_odd = 0
    
    # Loop through list of integers
    for num in list_of_num:
        # Sum up even numbers
        if num % 2 == 0:
            sum_even = sum_even + num
        # Sum up odd numbers
        else: sum_odd = sum_odd + num

    # Return list if even numbers and odd numbers

    return [sum_even, sum_odd]

"""
# Tests

lst = [1,2,3,4,5,6]
lst1 = [-2,12,34,56]
lst2 = [0,123,456,789]

print ("This works: " , sum_even_odd(lst))
print ("There's a negative integer here: ", sum_even_odd(lst1))
print ("There's a Zero here: ", sum_even_odd(lst2))
"""