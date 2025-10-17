'''
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas para ela:
Ex: Qual é o seu nome?
João da Silva, Olá João da Silva, é um prazer te conhecer!
Autor:Jules do Nascimento Pires
Ex:002
Data:15/10/2025
'''

# Entrada do nome
nome = str(input("Qual é o seu nome?"))

# Mostra o resultado
print("Olá {}, é um prazer te conhecer!".format(nome))
