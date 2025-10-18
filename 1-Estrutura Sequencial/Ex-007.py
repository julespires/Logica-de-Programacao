'''
Faça um programa que receba três números, calcule e mostre a multiplicação desses números.
Autor:Jules do Nascimento Pires
Ex:007
'''

# Entrada dos números
num1 = int(input("Primeiro número:"))
num2 = int(input("Segundo número:"))
num3 = int(input("Terçeiro número:"))

# Calcula a multiplicação
multiplicacao = num1 * num2 * num3

# Mostra o resultado
print("A multiplicação entre:{} * {} * {} = {}".format(num1, num2, num3, multiplicacao))