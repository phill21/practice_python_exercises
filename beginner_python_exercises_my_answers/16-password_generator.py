"""
Note: this is a 4-chili exercise, not because it introduces a concept, but because this exercise is more like a project.
Feel free to skip this and come back when you’re more ready!

Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import random
import string



#
# items = [1, 2, 3, 4, 5, 6, 7]
# random.shuffle(items)

#Contador de caracteres. Validar se parametros de senha ultrapassam o limite de digitos da senha
def count_char():
    ...

def char_generate_pass(param1):
    # Utilizar esse caso queira remover acentos e caracteres complexos
    # char_pass = random.sample(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '.', '?', '+'], k=param1)

    char_pass = random.choices(string.punctuation, k=param1)
    return ''.join(char_pass)

def num_generate_pass(param2):
    num_pass = random.choices(string.digits, k=param2)
    return ''.join(num_pass)

def alpha_generate_pass(param3):
    alpha_pass = random.choices(string.ascii_letters, k=param3)
    return ''.join(alpha_pass)

def generate_pass(qtd_num, qtd_alpha, qtd_char):
    united_param = ''.join(num_generate_pass(qtd_num) + alpha_generate_pass(qtd_alpha) + char_generate_pass(qtd_char))
    united_param = list(united_param.strip())
    random.shuffle(united_param)
    new_pass = ''.join(united_param)
    return new_pass


print(generate_pass(3, 3, 3))
# new_pass = ''.join(num_generate_pass(0) + alpha_generate_pass(3))
# print(new_pass)
# a = list(new_pass.strip())
# random.shuffle(a)
# b = ''.join(a)
# print(b)