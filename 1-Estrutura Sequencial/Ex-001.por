/*
 Faça um programa que receba quatro números inteiros, calcule e mostre a soma desses números.
 Autor:Jules do Nascimento Pires
 Ex:001
*/
programa {
  funcao inicio() {
    
    // Guarda os valores
    inteiro n1, n2, n3, n4
    
    // Entrada dos valores
    escreva("Primeiro valor:")
    leia(n1)
    escreva("Segundo valor:")
    leia(n2)
    escreva("Terçeiro valor:")
    leia(n3)
    escreva("Quarto valor:")
    leia(n4)
    
    // Limpa a tela
    limpa()
    
    // Calcula a soma
    inteiro soma = n1 + n2 + n3 + n4
    
    // Mostra a soma para o usuário
    escreva("Soma dos valores:" + soma)
  }
}
