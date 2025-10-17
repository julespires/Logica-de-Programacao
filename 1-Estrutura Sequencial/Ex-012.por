/*
Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.
Autor:Jules do Nascimento Pires
Ex:012
*/
programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    
    // Guarda os valores
    inteiro num1, num2
    
    // Recebe do usuário os valores
    escreva("INFORME DOIS VALORES MAIOR QUE ZERO\n")
    escreva("Primeiro valor:")
    leia(num1)
    escreva("Segundo valor:")
    leia(num2)
    
    // Limpa a tela
    limpa()
    
    // Calcula os valores elevado a pontencia de cada um
    inteiro elev1 = mat.potencia(num1, num2)
    inteiro elev2 = mat.potencia(num2, num1)
    
    // Mostra o resultado da operação
    escreva("O numero " + num1 + " elevado a potencia de " + num2 + " = " + elev1 + "\n")
    escreva("O número " + num2 + " elevado a potencia de " + num1 + " = " + elev2)
  }
}
