/*
Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = p * R2.
Autor:Jules do Nascimento Pires
Ex:010
Data:08/10/2025
*/
programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    
    real raio
    const real PI = 3.14

    escreva("Informe o valor do raio:")
    leia(raio)

    real area = PI * mat.potencia(raio,2)

    escreva("Área do círculo:" + area + "Cm")
  }
}
