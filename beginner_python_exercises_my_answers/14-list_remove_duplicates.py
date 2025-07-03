"""
Write a program (function!) that takes a list and returns a new list that contains all the elements
of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""
a = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7]
b = []
def for_remove_duplicates(lista):
    for i in lista:
        if i not in b:
            b.append(i)

def sets_remove_duplicates(lista):
    new_lista = set(lista)
    return new_lista


for_remove_duplicates(a)
print(b)

print(sets_remove_duplicates(a))