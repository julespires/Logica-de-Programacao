/*
Faça um programa que calcule e mostre a área de um triângulo. Sabe-se que: Área = (base * altura)/2.
Autor:Jules do Nascimento Pires
Ex:009
Data:08/10/2025
*/
programa {
  funcao inicio() {
    
    real base, altura

    escreva("Informe a base do triângulo:")
    leia(base)
    escreva("Informe a altura do triângulo")
    leia(altura)

    real area = (base * altura)/2

    escreva("Área do triângulo:" + area + "Cm")
  }
}
