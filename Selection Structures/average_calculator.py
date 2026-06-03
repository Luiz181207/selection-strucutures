print(10*'<', 'Média de 3 notas', 10*'>')
print('Obs: média=70')

n1=float(input('Digite a 1º nota:'))
n2=float(input('Digite a 2º nota:'))
n3=float(input('Digite a 3º nota:'))

if (n1+n2+n3)/3>=70:
    print('Você foi aprovado!\nsua média foi {:.2f}'.format((n1+n2+n3)/3))
else:
    print('Você foi reprovado!\nsua média foi {:.2f}'.format((n1+n2+n3)/3))
