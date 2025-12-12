'''
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se
que este sofreu um aumento de 25%.
Autor:Jules do Nascimento Pires
Ex:012
Data:03/01/2025
'''

# Biblioteca de sistema
import os
os.system('cls')

# Entrada do salário
salario = float(input('Informe seu salário: R$'))

# Calcula o aumento e o salário
aumento = salario * 0.25
novoSalario = salario + aumento

# Mostra o resultado
print('-' * 55)
print('Seu novo salário com aumento de R${} será de {}'.format(aumento, novoSalario))
print('-' * 55)