"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
 Print back to the user the same string, except with the words in backwards order.
 For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""

a = input('Type a phrase with 3 words or more: ')

def reverse_phrase(phrase):
    new_phrase = " ".join(phrase.split(" ")[::-1])
    return new_phrase

print(reverse_phrase(a))
