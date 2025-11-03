'''
<<<<<<< HEAD
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

=======
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
>>>>>>> aedd4553a8319d0c9b7b36f0dc1722470db134af
