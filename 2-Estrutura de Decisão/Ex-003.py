'''
Faça um programa que receba dois números e mostre o menor.
Autor:Jules do Nascimento Pires
Ex-003
Data:23/10/2025
'''
# Biblioteca
import os

# Guarda os números
num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))

# Limpa a tela
os.system('cls')

# CCondições
if (num1 < num2):
    print("O número {} é menor!".format(num1))

elif (num2 < num1):
    print("O número {} é menor!".format(num2))

else:
    print("Os números são iguais!")