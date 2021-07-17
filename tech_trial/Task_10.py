#! /usr/bin/env python3

def famous_letter(word):
    """
    Returns the letter with most occurences in a word and the number of occurences

        Parameters: 
            word (str): A string 
            
        Returns:
            A dictionary or list of dictionaries, most popular letter and number of occurences.   
    """
    # Initialise a dictionary to hold each letter and number of occurence
    occurences = {}

    # Iterate through the string
    for l in word:
        if l not in occurences.keys():
            occurences[l] = 1
        else:
            occurences[l] = occurences[l] + 1
    
    max_value = 0
    max_letter = ""
    max_list = []
    for key, value in occurences.items():
        if value > max_value:
            max_value = value
            max_letter = key
    
    max_list = []

    number_max_letter = list(occurences.values()).count(max_value)
    for key, value in occurences.items():
        if value == max_value:
            max_value = value
            max_letter = key
            max_list.append({max_letter:max_value})

    if len(max_list) > 1:
        return max_list
    else: 
        return max_list[0]

# Tests

print (famous_letter("abracadabra"))
print (famous_letter("abbbbbracadabbbbbbbra"))
print (famous_letter("abbbracadabbbraa"))
print (famous_letter("abbbracadabbbraaccccc"))