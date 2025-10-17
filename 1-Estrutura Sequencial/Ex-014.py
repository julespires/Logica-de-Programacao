'''
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: A = ((base maior + base menor) * altura)/2
Autor:Jules do Nascimento Pires
Ex-014
Data:14/10/2025
'''

# Entrada dos valores
baseMaior = float(input("Informe o valor da base maior:"))
baseMenor = float(input("Informe o valor da base menor:"))
altura = float(input("Informe o valor da altura:"))

# Cálculo da área
area = ((baseMaior + baseMenor) * altura)/2

# Mostra o resultado
print("Área do trapézio:{}".format(area))