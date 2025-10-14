'''
Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre
o valor do aumento e o novo salário.
Autor:Jules do Nascimento Pires
Ex:004
Data:01/10/2025
'''

# Entrada dos dados
salario = float(input("Informe o salário:R$"))
percentual = float(input("Informe o percentual de aumento:"))

# Calcula o novo salário
aumento = salario * percentual / 100
novoSalario = salario + aumento

# Mostra o resultado
print("=" * 35)
print("Aumento: R${}".format(aumento))
print("Novo salário: R${}".format(novoSalario))
print("=" * 35)           