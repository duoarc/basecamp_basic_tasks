#! /usr/bin/env python3

def replace_spaces(sentence):
    """
    Returns the sentence with all the spaces replaced

        Parameters: 
            sentence (str): A sentence, tense or phrase 

        Returns:
            The sentence after replacing all spaces with %20
    """

    # Replace all spaces
    return sentence.replace(" ", "%20")

# Tests

print (replace_spaces("othing added to commit but untracked files present (use git add to track)"))