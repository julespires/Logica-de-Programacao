'''
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário com
aumento de 25%.
Autor:Jules do Nascimento Pires
Ex:004
Data:03/10/2025
'''

salario = float(input("Salário do Funcionário R$:"))

aumento = salario * 25 / 100
novoSalario = salario + aumento

print("O novos salário com aumento de 25% será de {}".format(novoSalario))