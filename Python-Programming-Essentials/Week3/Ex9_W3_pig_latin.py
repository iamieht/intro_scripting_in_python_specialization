"""
Compute a (simplified) Pig Latin version of a word.
"""

###################################################
# Pig Latin function
def pig_latin(word):
    """
    Returns the (simplified) Pig Latin version of the word.
    """

    # Partial code for body
    first_letter = word[0]
    rest_of_word = word[1 : ]

    # Student should complete function on the next lines
    if first_letter not in 'aeiou':
        return rest_of_word + first_letter + 'ay'
    else:
        return word + 'way'
    

###################################################
# Tests
# Student should not change this code.
    
word = "pig"
print(pig_latin(word))

word = "owl"
print(pig_latin(word))

word = "python"
print(pig_latin(word))

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#igpay
#owlway
#ythonpay
