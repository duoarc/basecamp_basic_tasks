#! /usr/bin/env python3

import Task_2

def list_primes(list_of_num):
    """
    Returns a list of prime numbers

        Parameters: 
            list_of_num (list): List of positive integers 

        Returns:
            list_prime (list): List of prime numbers in list_of_num
    """

    # Check if the list of integers has any negative numbers
    for num in list_of_num:
        if num < 0:
            return "Please provide positive numbers only and try again"
    
    # Handle Zeroes
    if 0 in list_of_num:
        return "Please provide positive numbers only and try again. Zero is not a positive number!" 

    # Initialise variable to hold prime numbers
    list_prime = []

    # Loop over list numbers in list
    for num in list_of_num:
        # Check number is a prime number
        if Task_2.is_prime(num):
            # Append number to prime number list if it is prime
            list_prime.append(num)

    # Return prime number list
    return list_prime

print(list_primes([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]))