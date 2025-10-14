'''
Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu salário final.
Autor:Jules do Nascimento Pires
Ex:011
'''

# Entrada do salário e vendas
salario = float(input("Informe o salário do funcionário:R$"))
vendas = float(input("Informe o valor das vendas:"))

# Calculo da comissão e novo salário
comissao = vendas * 4 / 100
novoSalario = salario + comissao

# Mostra o valor da comissão e do novo salário
print("Valor da comissão: R$ {}".format(comissao))
print("Valor do novo salário: R$ {}".format(novoSalario))
