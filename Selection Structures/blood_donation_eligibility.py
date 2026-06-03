ano=int(input('Informe o ano de nascimento?'))
idade = 2026-ano
if idade>18 and idade<59:
    print('Essa pessoa pode doar sangue!')
else:
    print('Essa pessoa não pode doar sangue!\nfaltam {} anos para poder doar'.format(18-idade))
