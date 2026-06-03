"""Média de aproveitamento      Conceito
Entre 9.0 e 10.0                A
Entre 7.5 e 9.0                 B
Entre 6.0 e 7.5                 C
Entre 4.0 e 6.0                 D
Entre 4.0 e zero                E

Caso, o conceito seja abaixo de C, indique reprovado, caso contrário aprovado."""

n1 = float(input('Digite a 1º nota:'))
n2 = float(input('Digite a 2º nota:'))
n3 = float(input('Digite a 3º nota:'))
media = (n1+n2+n3)/3
print('Média: {:.2f}'.format(media))
if media>=9 and media<=10:
    conceito = 'A'
elif media>=7.5 and media<9:
    conceito = 'B'
elif media>=6 and media<7:
    conceito = 'C'
elif media>=4 and media<6:
    conceito = 'D'
elif media<4:
    conceito = 'E'

print('A sua média foi {:.2f}\nConceito {}'.format(media,conceito))

if media>6:
    print('Aprovado!')
else:
    print('Reorovado!')
