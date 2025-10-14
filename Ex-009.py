'''
Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando
peso 2 para a primeira e peso 3 para a segunda.
Autor:Jules do Nascimento Pires
'''

# Entrada das notas
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

# Calculo da média ponderada
media = (nota1 * 2 + nota2 * 3) / (2 + 3)

# Resultado da média
print("Média ponderada das notas:{}".format(media))