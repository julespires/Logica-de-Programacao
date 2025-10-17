'''
Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
Ex: Nome do Funcionário: Maria do Carmo
Salário: 1850,45.
O funcionário Maria do Carmo tem um salário de R$1850,45 em junho.
Autor:Jules do Nascimento Pires
Ex:003
Data:15/10/2025
'''

nome = str (input("Nome do funcionário:"))
salario = float(input("Salário do funcionário:R$"))

print("O funcionário {} tem um salário de: R${}".format(nome, salario))