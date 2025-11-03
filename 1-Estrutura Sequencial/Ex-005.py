'''
Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre
o valor do aumento e o novo salário.
Autor:Jules do Nascimento Pires
Ex:005
Data:01/11/2025
'''
# Utilização da biblioteca OS
import os

# Limpa a tela
os.system('cls')

# Recebe o salário e o percentual de aumento
salario = float(input('Salário do Funcionário:R$'))
percentualAumento = float(input('Percentual de aumento: %'))

# Calcula o aumento e o salário
aumento = salario * percentualAumento / 100
novoSalario = salario + aumento

# Mostra o resultado do aumento e o novo salário
print('Valor do aumento: R${:.2f}'.format(aumento))
print('Novo salário:R${:.2f}'.format(novoSalario))