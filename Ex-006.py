'''
Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber,
sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% tam-
bém sobre o salário base.
Autor:Jules do Nascimento Pires
Ex:005
Data:26/10/2025
'''

# Recebe o salário
salario = float(input("Salário do Funcionário: R$"))

# Cálculos
imposto = 7 / 100
gratificacao = 5 / 100
novoSalario = salario + gratificacao - imposto

# Mostra o novo salário
print("Novo salário: R${}".format(novoSalario))