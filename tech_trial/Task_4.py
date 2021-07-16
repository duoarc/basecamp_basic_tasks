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

    if password.isalpha():
        return 0
    elif password.isnumeric():
        return 1
    elif password.isalnum():
        return 2
    else:
        return 3


# Tests

print ("dsfghjkl", passwd_strength("dsfghjkl"))
print ("123456", passwd_strength("123456"))
print ("dsfghjkl123456", passwd_strength("dsfghjkl123456"))
print ("dsfghjkl123456@#$%^", passwd_strength("dsfghjkl123456@#$%^"))
