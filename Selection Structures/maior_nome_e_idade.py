nome1=input('Qual é seu nome?')
idade1=int(input('Qual é sua idade?'))
print(' ')

nome2=input('Qual é o outro nome?')
idade2=int(input('Qual é a outra idade?'))
print(' ')

#como saber qual string é maior? len() conta quantos caracteres existem em uma string
if len(nome1)>len(nome2):
    print('A pessoa com o nome mais longo é {}'.format(nome1))
else:
    print('A pessoa com o nome mais longo é {}'.format(nome2))

if idade1>idade2:
    print('A pessoa mais velha é {}'.format(nome1))

if idade2>idade1:
    print('A pessoa mais velha é {}'.format(nome2))

if idade1==idade2:
    print('As pessoas têm a mesma idade')
