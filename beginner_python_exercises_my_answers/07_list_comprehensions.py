""""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a_par = []

def compara_par(lista):
    for num in lista:
        if num % 2 == 0:
            a_par.append(num)
    return a_par

print(compara_par(a))

# mesmo código em uma linha
a_par2 = [num for num in a if num % 2 == 0]
print(a_par2)
