n1=int(input('Digite um número:'))
n2=int(input('Digite outro número:'))

#Só o maior número:
#if n1>n2:
#    print(f'O maior número é {n1}')
#else:
#    print(f'O maior número é {n2}')

#Maior e menor número:
if n1>n2:
    print('O maior número é {}\ne o menor número é {}'.format(n1,n2))
else:
    print('O maior número é {}\ne o menor é {}'.format(n2,n1))
