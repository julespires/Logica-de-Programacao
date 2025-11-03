'''
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se
que este sofreu um aumento de 25%.
Autor:Jules do Nascimento Pires
Ex:004
Data:01/11/2025
'''

# Utilização da biblioteca OS
import os

# Limpa a tela
os.system('cls')

# Entrada do salário
salario = float(input('Salário do Funcionário R$:'))

# Calcula o aumento e o novo salário
aumento = salario * 25 / 100
novoSalario = salario + aumento

# Mostra o salário com aumento de 25%
print("Novo salário com aumento de 25% R$:{:.2f}".format(novoSalario))