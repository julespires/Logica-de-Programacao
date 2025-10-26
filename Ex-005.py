'''
Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre
o valor do aumento e o novo salário.
Autor:Jules do Nascimento Pires
Ex:005
Data:26/10/2025
'''

# Entrada de dados
salario = float(input("Salário do Funcionário: R$"))
percAumento = float(input("Percentual de aumento:"))

# Calculos
aumento = salario * percAumento / 100
novoSalario = salario + aumento

# Mostra o resultado
print("Valor do aumento: R${}".format(aumento))
print("Novo salário:{}".format(novoSalario))