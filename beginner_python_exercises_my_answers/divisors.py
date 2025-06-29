""""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

user_num = int(input('Digite um número inteiro para descobrir seus divisores: '))
list_divisores = []

def acha_divisores(numero):
    for x in range(1, numero):
        if numero % x == 0:
            list_divisores.append(x)

    return list_divisores

print(acha_divisores(user_num))