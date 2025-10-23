'''
Faça um programa que receba duas notas, calcule e mostre a média aritmética e a mensagem que se encontra
na tabela a seguir:
MÉDIA ARITIMÉTICA                    MENSAGEM
0.0--------3.0                       Reprovado
3.0--------7.0                       Exame
7.0--------10.0                      Aprovado
'''

import os



# Entrada das notas
nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))

os.system('cls')

# Calcula a média
media = (nota1 + nota2) / 2

# Mostra o resultado
print("Média aritimética das notas:{:.2f}".format(media))

# Condições
if (media >= 0.0 and media < 3.0):
    print("Reprovado")

elif (media >= 3.0 and media < 7.0):
    print("Fazer exame!")

elif (media >= 7.0 and media <= 10.0):
    print("Aprovado!")

else:
    print("Opção inválida!")