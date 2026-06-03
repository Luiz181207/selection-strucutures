import datetime
hoje = datetime.date.today()
dia = int(input('Em que dia você nasceu?'))
mes = int(input('Em que mês você nasceu?'))
ano = int(input('Em que ano você nasceu?'))
nascimento = datetime.date(ano, mes, dia)
anv_16 = datetime.date(ano+16, mes, dia)
#anv_16 seria quando o usuário completa 16 anos, então if hoje>=data_16 verifica se o dia de hoje já passou da data de aniversário
if hoje >=anv_16:
    print('Você já pode votar!')
else:
    print('Você ainda não pode votar!')
