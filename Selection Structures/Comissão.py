"""    a. 5%, para vendas até R$ 100,00
    b. 6% para vendas até R$ 500,00
    c. 7% para vendas até R$ 1000,00
    d. 8% para vendas acima de R$ 1000,00

Implemente um algoritmo que calcule a comissão do vendedor."""

valor = float(input('Digite o valor da venda: R$'))

if valor>0 and valor<=100:
    tx = 0.05
    #comissão = valor * 0.05
elif valor>100 and valor<=500:
    tx = 0.06
    #comissão = valor * 0.06
elif valor>500 and valor<=1000:
    tx = 0.07
    #comissão = valor * 0.07
elif valor>1000:
    tx = 0.08
    #comissão = valor * 0.08

comissão = valor * tx
print('O valor da comissão é de R${:.2f}'.format(comissão))