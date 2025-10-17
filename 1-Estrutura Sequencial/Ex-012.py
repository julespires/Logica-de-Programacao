'''
Faça um programa que receba o peso de uma pessoa, calcule e mostre:
a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.
Autor:Jules do Nascimento Pires
Ex:012
'''

# Entrada do peso
peso = float(input("Qual é o seu peso?"))

# Calcula o peso com aumento
peso15 = peso + peso * 15 / 100
peso20 = peso + peso * 20 / 100

# Mostra o resultado
print("Seu peso se você engordar 15%:{}".format(peso15))
print("Seu peso se você engordar 20%:{}".format(peso20))