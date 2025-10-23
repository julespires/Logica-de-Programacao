'''
Faça um programa que receba dois númerso informados pelo usuário imprima e mostre o maior deles.
Autor:Jules do Nascimento Pires
Ex:001
Data:22/10/2025
'''

# Biblioteca de sistemas
import os

# Limpa a tela
os.system('cls')

# Guarda os números 
num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))

# Condições
if (num1 > num2):
    print("O número {} é maior!".format(num1))

else:
    print("O número {} é maior!".format(num2))