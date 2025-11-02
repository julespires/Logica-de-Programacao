'''
<<<<<<< HEAD
Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.
Autor:Jules do Nascimento Pires
Ex:005
Data:28/10/2025
'''

# Entrada das notas
nota1 = float(input("Primeira nota:"))
peso1 = int(input("Primeiro peso:"))
nota2 = float(input("Segunda nota:"))
peso2 = int(input("Sgundo peso:"))
nota3 = float(input("Terçeira nota:"))
peso3 = int(input("Terçeiro peso:"))

# Média ponderada
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) // (peso1 + peso2 + peso3)

# Mostra o resultado
print("Média ponderada das notas:{}".format(media))
=======
Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre
o valor do aumento e o novo salário.
Autor:Jules do Nascimento Pires
Ex:005
Data:26/10/2025
'''

# Entrada de dados
salario = float(input("Salário do Funcionário: R$"))
percAumento = float(input("Percentual de aumento:"))

# Calculos
aumento = salario * percAumento / 100
novoSalario = salario + aumento

# Mostra o resultado
print("Valor do aumento: R${}".format(aumento))
print("Novo salário:{}".format(novoSalario))
>>>>>>> aedd4553a8319d0c9b7b36f0dc1722470db134af
