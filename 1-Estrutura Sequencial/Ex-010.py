'''
Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.
Autor:Jules do Nascimento Pires
Ex:010
'''

# Entrada do preço do produto
precoProduto = float(input("Informe o preço do produto: R$"))

# Calcula o desconto e o novo preço
desconto = precoProduto * 10 / 100
novoPreco = precoProduto - desconto

# Mostra o novo preço com desconto
print("Novo preço com 10% de desconto: R${}".format(novoPreco))