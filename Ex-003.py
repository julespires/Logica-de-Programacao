'''
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se
que este sofreu um aumento de 25%.
Autor:Jules do Nascimento Pires
Ex:003
'''

# Entrada do salário
salario = float(input("Digite o salário:R$"))

# Calcula o aumento
aumento = salario / 100
novoSalario = salario + aumento

# Mostra o resultado
print("Novo salário: R${}".format(novoSalario))