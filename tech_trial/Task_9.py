#! /usr/bin/env python3

def is_palindrome(word):
    """
    Returns "Yes" if the word is a palindrome

        Parameters: 
            word (str): A string 
            
        Returns:
            A string[YES/NO], "YES" if the word is a palindrome and "No" otherwise 
    """
    # Iterate over half of the word
    for l in range(len(word)//2):
        # Compare each letter with the mirror
        if word[l] != word[-l-1]:
            # Return "No" if any letter is not the same as the mirror
            return "No"

    # Return "Yes" if a word Iterates through without throwing a "No"
    return "Yes"

# Tests
print (is_palindrome("racecar"))
print (is_palindrome("word"))
print (is_palindrome("madam"))
print (is_palindrome("strawwarts"))
print (is_palindrome("wait"))
print (is_palindrome("rotator"))
