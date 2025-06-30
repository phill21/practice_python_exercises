""""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
from random import randint

random_num = randint(1, 9)
contador_erro = 0
while True:
    user_imp = input('Jogo da adivinhação!!! Se quiser Sair do jogo, só digitar "exit" \n\nAdvinhe que número eu estou pensando: ')
    if user_imp == 'exit':
        print('Tudo bem! tentamos depois!')
        break

    u = int(user_imp)
    if u > random_num:
        print(f'Muito alto! Tente um número mais baixo!\n')
        contador_erro += 1
    elif u < random_num:
        print(f'Muito baixo! Tente um número mais alto!\n')
        contador_erro += 1
    else:
        print(f'Você acertou!! O número que pensei foi {random_num}!! \nNúmero de tentativas: {contador_erro}')
        break
