"""Pedra, papel e tesoura"""
import random
esc = str(input('Escolha pedra, papel ou tesoura:').strip().capitalize())
lista = ['Pedra','Papel','Tesoura']

bot = random.choice(lista)
print(f'Computador: {bot}')

def vit():
    print('\033[1;32mParabéns, você venceu!\033[m')
def der():
    print('\033[1;31mNão foi dessa vez!\033[m\nTente novamente!')

if bot == esc:
    print('\033[1;33mEmpate!')

elif esc == 'Tesoura':
    if bot == 'Papel':
        print(vit())
    elif bot == 'Pedra':
        print(der())
elif esc == 'Pedra':
    if bot == 'Papel':
        print(der())
    elif bot == 'Tesoura':
        print(vit())
elif esc == 'Papel':
    if bot == 'Pedra':
        print(vit())
    elif bot == 'Tesoura':
        print(der())
