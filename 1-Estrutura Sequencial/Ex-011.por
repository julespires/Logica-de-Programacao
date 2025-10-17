/*
Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
a) o número digitado ao quadrado;
b) o número digitado ao cubo;
c) a raiz quadrada do número digitado;
d) a raiz cúbica do número digitado.
Ex:11/10/2025
Data:09/10/2025
*/
programa {

  inclua biblioteca Matematica --> mat
  funcao inicio() {
    
    inteiro num, quad, raiz

    escreva("Digite um número inteiro maior que zero:")
    leia(num)
    
    limpa()
    
    escreva("O quadrado de " + num + " = " + mat.potencia(num,2) + "\n")
    escreva("O cubo de " + num + " = " + mat.potencia(num, 3) + "\n")
    escreva("A raiz quadrada de " + num + " = " + mat.raiz(num, 2) + "\n")
    escreva("A raiz cúbica de " + num + " = " + mat.raiz(num, 3) + "\n")
  }
}
