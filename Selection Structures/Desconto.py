#2000->3%
#2000-3000->4.5%
#3000-5000->5%
#5000-7000->6%
#>7000->7%

valor = float(input('Digite o valor do produto: R$'))
if valor<=0:
    print('Valor inválido')
if valor<=2000 and valor>0:
    desconto = valor * 0.03
elif valor>2000 and valor<=3000:
    desconto = valor * 0.045
elif valor>3000 and valor<=5000:
    desconto = valor * 0.05
elif valor>5000 and valor<=7000:
    desconto = valor * 0.06
elif valor>7000:
    desconto = valor * 0.07

valor_final = valor - desconto
print('O valor final fica R${:.2f}, com um desconto de R${:.2f}'.format(valor_final,desconto))
