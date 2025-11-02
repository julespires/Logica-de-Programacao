'''
Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre
o valor do aumento e o novo salário.
Autor:Jules do Nascimento Pires
Ex:007
Data:28/10/2025
'''

# Entrada do Salário e do percentual de aumento
salario = float(input("Salário do Funcionário R$:"))
percentual = float(input("Informe o percentual de aumento:"))

# Calcula o aumento e novo salário
aumento = salario * percentual / 100
novoSalario = salario + aumento

# Mostra o valor do aumento e do novo salário
print("Aumento: R${}".format(aumento))
print("Novo salário: R${}".format(novoSalario))