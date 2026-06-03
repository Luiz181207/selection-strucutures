"""• Telefonou para a vítima? [S/N]
• Esteve no local do crime? [S/N]
• Mora perto da vítima? [S/N]
• Tinha algum dívida com a vítima? [S/N]
• Já trabalhou com a vítima? [S/N]

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”.
Entre 3 e 4 como “Cúmplice” e 5 como “Assassino“.
Caso contrário, ele será classificado como “Inocente“. """

pontos = 0
print('Uma pessoa foi assasinada e você foi apontado como suspeito,\nresponda com sinceridade as próximas perguntas')

r1 = input('Você telefonou para a vítima? [S/N]:').upper().strip()
r2 = input('Você esteve no local do crime? [S/N]:').upper().strip()
r3 = input('Você mora perto da vítma? [S/N]:').upper().strip()
r4 = input('Você tinha alguma dívida com a vítma? [S/N]:').upper().strip()
r5 = input('Você já trabalhou com a vítima? [S/N]:').upper().strip()

if r1 == 'S':
    pontos = pontos + 1
if r2 == 'S':
    pontos = pontos + 1
if r3 == 'S':
    pontos = pontos + 1
if r4 == 'S':
    pontos = pontos + 1
if r5 == 'S':
    pontos = pontos + 1

if pontos<2:
    print('Você é inocente!')
elif pontos == 2:
    print('Você é suspeito!')
elif pontos == 3 or pontos == 4:
    print('Você é cúmplice!')
elif pontos == 5:
    print('Você é culpado!')
