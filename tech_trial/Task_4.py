#! /usr/bin/env python3

def passwd_strength(password):
    """
    Returns an integer between 0-3 that indicates the strength of the password input

        Parameters: 
            password (UTF-8): A password 

        Returns:
            0 -> very weak e.g. a password with only strings
            1 -> weak e.g. a password with only numbers
            2 -> strong e.g. a password containing strings and numbers
            3 -> very strong e.g. a password containing strings, numbers and special characters (!,@,#,$,%, etc)
    """
    # Check if the password comprises of only alphabets
    if password.isalpha():
        return 0
    # Check if the password comprises of only numbers
    elif password.isnumeric():
        return 1
    # Check if the password comprises of only alphabets and numbers
    elif password.isalnum():
        return 2
    # Password that do not satisfy the conditions above contain symbols or special characters
    else:
        return 3

"""# Tests

print ("dsfghjkl", passwd_strength("dsfghjkl"))
print ("123456", passwd_strength("123456"))
print ("dsfghjkl123456", passwd_strength("dsfghjkl123456"))
print ("dsfghjkl123456@#$%^", passwd_strength("dsfghjkl123456@#$%^"))
"""