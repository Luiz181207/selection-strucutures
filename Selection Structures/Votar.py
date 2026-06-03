#Valor booleano: true/false
ano=int(input('Em que ano você nasceu?'))
idade=2026-ano

print('Você tem {} anos'.format(idade))

#decisão sobre votar 16(anos)
if idade>=16:
    print('Você já pode votar!')
else:
    print('Você ainda não pode votar')
    print('Falta(m) {} ano(s) pra você poder votar'.format(16-idade))
#arrumar o cálculo da idade