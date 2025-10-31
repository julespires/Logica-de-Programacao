'''
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