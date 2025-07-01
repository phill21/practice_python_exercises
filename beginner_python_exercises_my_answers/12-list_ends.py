"""
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

a = [5, 10, 15, 20, 25]

def lista_first_last(lista):
    new_lista = []
    new_lista.append(lista[0])
    new_lista.append(lista[-1])
    return new_lista

print(lista_first_last(a))
