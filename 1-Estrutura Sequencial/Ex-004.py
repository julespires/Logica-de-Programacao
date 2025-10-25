'''
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se
que este sofreu um aumento de 25%.
Autor:Jules do Nascimento Pires
Ex:004
Data:23/10/2025
'''

# Entrada do salario
salario = float(input("Informe o salário:"))

# Calcula o novo aumento e o novo salário
aumento = salario * 25 / 100
novoSalario = salario + aumento

# Mostra o novo salário 
print("Novo salário com aumento de 25%:{}".format(novoSalario))