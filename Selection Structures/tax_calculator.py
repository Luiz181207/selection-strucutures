"""      Salário             IRPF
Até R$1.903,98            Isento
De R$1.903,99 até R$2.826,65    7,5%
De R$2.826,66 até R$3.751,05    15%
De R$3.751,06 até R$4.664,68    22,5%"""
sal = float(input('Digite seu salário: R$'))
if sal<=1903.98:
    print('\033[1;32mIsento de imposto de renda')
else:
    print('Calculando immposto...')
    from time import sleep
    sleep(1)
    if sal>1903.98 and sal<=2826.65:
        imposto = sal * 7.5/100
    elif sal>2826.65 and sal<=3751.05:
        imposto = sal * 15/100
    elif sal>3751.05 and sal<=4664.68:
        imposto = sal * 22.5/100
    print('O valor do imposto a recolher é \033[31mR${:.2f}\033[m'.format(imposto))
