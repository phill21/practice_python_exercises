a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_number = int(input('Digite um número: '))
new_list = []
def compara_lista(lista):
    for numero in lista:
        if numero < user_number:
            new_list.append(numero)
    return new_list

print(compara_lista(a))
