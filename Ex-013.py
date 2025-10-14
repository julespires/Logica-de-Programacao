'''
Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas.
Autor:Jules do Nascimento Pires
Ex:013
'''

# Entrada do peso
peso = float(input("Qual é o seu peso atual:"))

# Converte em gramas
gramas = peso * 1000

# Mostra o peso convertido em gramas
print("O seu peso de {} em gramas é {}".format(peso, gramas))