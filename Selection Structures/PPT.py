"""Pedra, papel e tesoura"""
import random
esc = str(input('Escolha pedra, papel ou tesoura:').strip().capitalize())
lista = ['Pedra','Papel','Tesoura']

bot = random.choice(lista)
print(f'Bot: {bot}')

if bot == esc:
    print('Empate!')

elif esc == 'Tesoura':
    if bot == 'Papel':
        print('Você venceu!')
    elif bot == 'Pedra':
        print('Você perdeu!')

elif esc == 'Pedra':
    if bot == 'Papel':
        print('Você perdeu!')
    elif bot == 'Tesoura':
        print('Você venceu!')

elif esc == 'Papel':
    if bot == 'Pedra':
        print('Você venceu!')
    elif bot == 'Tesoura':
        print('Você perdeu!')


