'''
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se
que este sofreu um aumento de 25%.
Autor:Jules do Nascimento Pires
Ex:006
'''

# Entrada do salário do funcionáriio
salario = float(input("Salário do funcionário: R$"))

# Calcula o aumento e o novo salário
aumento = salario * 25 / 100
novoSalario = salario + aumento

# Mostra o novo salário
print("Novo salário:: R${:.2f}".format(novoSalario))

