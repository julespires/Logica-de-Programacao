'''
Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber,
sabendo-se que o funcionário tem gratificação de R$ 50 e paga imposto de 10% sobre o salário base.
Autor:Jules do Nascimento Pires
Ex:007
Data:02/11/2025
'''

# Utilização da biblioteca de sistema
import os

# Limpa a tela
os.system('cls')

# Recebe o salário
salario = float(input('Salário: R$'))

# Calcula o salário
imposto = salario * 10 / 100
novoSalario = salario + 50 - imposto

# Mostra o novo salário
print('Novo salário: R${:.2f}'.format(novoSalario))