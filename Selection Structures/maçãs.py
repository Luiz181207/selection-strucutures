qtd=int(input('Quantas maçãs você deseja comprar?'))
if qtd<12:
    print('O preço da maçã é R$0,30')
    print('O valor de {} maçã(s) é R${:.2f}'.format(qtd,qtd*0.30))

if qtd>=12:
    print('O preço da maçã é R$0,25')
    print('O valor de {} maçã é R${:.2f}'.format(qtd,qtd*0.25))
