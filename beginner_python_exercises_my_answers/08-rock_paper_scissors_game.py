""""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
from random import randint
options = ['pedra', 'papel', 'tesoura']
while True:
    computador = randint(0, 2)
    user_imp = int(input(f'[0] Pedra \n[1] Papel \n[2] Tesoura \nSelecione uma opção: '))
    print(10 * '=-')
    print(f'Computador: {options[computador]} \nSua escolha: {options[user_imp]}')
    print(10 * '=-')
    if user_imp == 0:
        if computador == 1:
            print('Você perdeu! Tente  novamente')
        elif computador == 2:
            print('Você ganhou!')
            break
        else:
            print('Empate! Tente  novamente')
    elif user_imp == 1:
        if computador == 2:
            print('Você perdeu! Tente  novamente')
        elif computador == 0:
            print('Você ganhou!')
            break
        else:
            print('Empate! Tente  novamente')
    elif user_imp == 2:
        if computador == 0:
            print('Você perdeu! Tente  novamente')
        elif computador == 1:
            print('Você ganhou!')
            break
        else:
            print('Empate! Tente  novamente')
    else:
        print('Opção inválida! Tente  novamente')


