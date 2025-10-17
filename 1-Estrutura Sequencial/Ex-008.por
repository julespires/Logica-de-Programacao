/*
Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o
valor do rendimento e o valor total depois do rendimento.
Autor:Jules do Nascimento Pires
Ex:008
Data:08/10/2025
*/
programa {
  funcao inicio() {
    
    // Guarda o salário e a taxa de juros
    real deposito, taxa
    
    // Entrada dos dados
    escreva("Informe o valor do depósito:")
    leia(deposito)
    escreva("Informe o valor da taxa de juros:")
    leia(taxa)
    
    // Cálculo
    real rendimento = deposito * taxa / 100
    real total = deposito + rendimento
    
    // Mostra o rendimento e o valor total
    escreva("Valor do rendimento: R$" + rendimento + "\n")
    escreva("Valor total: R$" + total)
  }
}
