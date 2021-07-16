#! /usr/bin/env python3

def is_prime(num):
    """
    Returns True if the number is a prime number

        Parameters: 
            num (int): A positive integer 

        Returns:
            True for prime number and False for non-prime number
    """

    # Check if the number is a negative number or zero

    if num <= 0:
        return "Please provide positive numbers only and try again. Zero is not a positive number!"
    
    # Handle numbers 1 and 2
    if num == 1:
        return False
    
    if num == 2:
        return True


    # Loop through numbers from two to the positive integer
    for n in range(2,num):

        # If the number is divisible by any number, exit the function and return False
        if num%n == 0:
            return False
        
        # If it is not sivisible by the number in the loop move to the next iteration
        else:
            continue 
    
    # If the loop run through all the numbers less than the positive integer without finding a factor, then it is a prime number. Yaay!
    return True

# Tests

"""print ("Is {} a prime number? {}".format(2, is_prime(2)))
print ("Is {} a prime number? {}".format(3, is_prime(3)))
print ("Is {} a prime number? {}".format(17, is_prime(17)))
print ("Is {} a prime number? {}".format(5, is_prime(5)))
print ("Is {} a prime number? {}".format(20, is_prime(20)))
print ("Is {} a prime number? {}".format(19, is_prime(19)))
print ("Is {} a prime number? {}".format(25, is_prime(25)))
print ("Is {} a prime number? {}".format(89, is_prime(89)))"""