"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# usando set
def compara_listas(lista_1, lista_2):
    return list(set(lista_1) & set(lista_2))

print(compara_listas(a, b))


# usando For
newlist = []
def compara_listas_for(lista1, lista2):
    for num in lista2:
        if num in lista1:
            newlist.append(num)
    return newlist
print(compara_listas_for(a, b))


# usando apenas uma linha
print([num for num in b if num in a])