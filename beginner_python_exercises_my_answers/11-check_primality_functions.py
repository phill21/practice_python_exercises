"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""
import math

user_imp = int(input("Digite um número para saber se ele é primo: "))
raiz_quadrada = math.sqrt(user_imp)

def num_isprimo(numero):
    if numero <= 1:
        return False
    for x in range(2, numero):
        if numero % x == 0:
            return False
        else:
            return True

# num_isprimo(user_imp)

if num_isprimo(user_imp):
    print(f'{user_imp} é primo!')
else:
    print(f'{user_imp} não é um número primo!')


# OUTRA SOLUÇÃO USANDO LIST COMPREHENSIONS
user_imp2 = int(input('Digite um número para saber se ele é primo: '))
lista_teste = [i for i in range(2, user_imp2) if user_imp2 % i == 0]

def is_primo(numero):
    if numero > 1:
        if len(lista_teste) == 0:
            print(f'{user_imp2} é um número primo!')
        else:
            print(f'{user_imp2} NÃO é um número primo!')

    else:
        print(f'{user_imp2} NÃO é um número primo!')

is_primo(user_imp2)
