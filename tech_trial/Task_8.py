#! /usr/bin/env python3

def count_threes(num):
    """
    Returns the number of integers that have a three in them which is less than or equal to num

        Parameters: 
            num (int): A positive integer
            
        Returns:
            A dictionary, the count of threes and the intergers with threes
    """
    # Initialise list to hold integers that have three in them
    num_with_three = []

    # Initialise count variable 
    count = 0

    # Run through each number less than num
    for n in range(num+1):
        # Check if the number had a 3 in it
        if "3" in str(n):
            # Save it in a list
            num_with_three.append(n)
            # Iterate through the number to count the threes
            for i in str(n):
                # Check if each digit is a 3
                if i == "3":
                    # Increase the count for each 3
                    count = count + 1

    # Return a dictionary showing the count of 3, and the list of numbers that has 3s        
    return { "count": count, "numbers": num_with_three}

"""
# Tests

print (count_threes(35))
"""