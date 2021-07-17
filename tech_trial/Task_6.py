#! /usr/bin/env python3

from itertools import combinations

def sum_in_array(list_num, tsum):
    """
    Returns a list of three numbers that sum up to tsum

        Parameters: 
            list_num (list): A list of positive integers
            tsum (int): A target sum

        Returns:
            A list of three positive integers.
    """

    # Get all the combinations of 3 integers in the list
    combinations_list = combinations(list_num,3)

    # Iterate over all the combinations
    for comb in list(combinations_list):
        # Check if the sum of each combination is equal to the target sum 
        if sum(comb) == tsum:
            # Return the combination that meets the requirement 
            return list(comb)

    # If no combination meets the requirement, the code come here to return -1
    return -1

"""# Tests

print (sum_in_array([1,2,3,4,5,6], 6))
print (sum_in_array([1,2,3,4,5,6], 666))
print (sum_in_array([1,2,3,4], 9))"""