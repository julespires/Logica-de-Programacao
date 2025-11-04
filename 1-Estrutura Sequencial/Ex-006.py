'''
Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber,
sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% também
sobre o salário base.
Autor:Jules do Nascimento Pires
Ex:006
Data:02/11/2025
'''

# Biblioteca de sistema
import os

# Limpa a tela
os.system('cls')

# Recebe o salário
salario = float(input('Salário: R$'))

# Realiza os calculos
graticacao = 5 / 100
imposto = 7 / 100
novoSalario = salario + graticacao - imposto

# Mostra o resultado
print('Novo salário:{:.2f}'.format(novoSalario))