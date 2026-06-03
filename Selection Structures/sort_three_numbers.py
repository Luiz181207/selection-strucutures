""" Escreva um programa Python que ordena três números em ordem crescente."""
n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número:'))
n3 = int(input('Digite o 3º número:'))
numeros = [n1,n2,n3]
print('Os números em ordem crescente é', sorted(numeros)) #sorted() coloca os números em ordem crescente
