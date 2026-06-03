""" Escreva um programa Python que ordena três números em ordem crescente."""
n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número:'))
n3 = int(input('Digite o 3º número:'))

if n1<n2 and n1<n3:
    if n2<n3:
        lista =[n1,n2,n3]
    elif n3<n2:
        lista = [n1,n3,n2]
elif n2<n1 and n2<n3:
    if n1<n3:
        lista = [n2,n1,n3]
    elif n3<n1:
        lista = [n2,n3,n1]
elif n3<n1 and n3<n2:
    if n1<n2:
        lista = [n3,n1,n2]
    elif n2<n1:
        lista = [n3,n2,n1]
print('Os números na ordem crescente é {}'.format(lista))
