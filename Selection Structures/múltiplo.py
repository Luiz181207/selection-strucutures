num=int(input('Digite um número:'))
m=int(input('Digite um múltiplo:'))

if m%num==0:
    print('O número {} é múltiplo de {}'.format(m,num))
else:
    print('O número {} não é múltiplo de {}'.format(m,num))

