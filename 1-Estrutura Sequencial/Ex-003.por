/*
Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.
Autor:Jules do Nascimento Pires
Ex:003
*/
programa {
  // Este programa utiliza a biblioteca Matematica
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    
    real n1, n2, n3 // Guarda as notas
    inteiro p1, p2, p3 // Guarda os pesos

    // Entrada das notas e do peso
    escreva("Primeira nota:")
    leia(n1)
    escreva("Primeiro peso:")
    leia(p1)
    escreva("Segunda nota:")
    leia(n2)
    escreva("Segundo peso:")
    leia(p2)
    escreva("Terçeira nota:")
    leia(n3)
    escreva("Terçeiro peso:")
    leia(p3)
    
    // Limpa a entrada das notas e do peso
    limpa()

    // Calcula a média ponderada
    real media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)
    
    // Mostra o resultado
    escreva("Média aritimética das notas:" + mat.arredondar(media, 2))
  }
}
