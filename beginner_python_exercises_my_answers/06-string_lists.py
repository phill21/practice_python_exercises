""""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""
def ispalindrome(word):
    compara = word == word[::-1]
    if compara:
        print(f'{word} é um palíndromo!')
    else:
        print(f'{word} não é um palíndromo!')


a = str(input('Digite uma palavra para descobrir se é um palíndromo: '))


ispalindrome(a)

