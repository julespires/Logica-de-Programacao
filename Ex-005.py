'''
Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber,
sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% também
sobre o salário base.
Autor:Jules do Nascimento Pires
Ex-005
'''

# Entrada do salário base
salarioBase = float(input("Digite o salário base: R$"))

# Cálculo
gratificacao = salarioBase * 5 / 100
imposto = salarioBase * 7 / 100
novoSalario = salarioBase + gratificacao - imposto

# Resultado
print("Novo salário: R${}".format(novoSalario))