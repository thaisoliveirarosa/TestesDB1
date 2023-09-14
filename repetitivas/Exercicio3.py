# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre.

contador = 0
numeroInteiro = 0

while contador < 2:
    contador = contador + 1
    numeroInteiro = numeroInteiro + int(input('Digite um número inteiro: '))

numeroReal = float(input('Digite um número real: '))

calculo = numeroInteiro + numeroReal

print('A soma dos números é:', calculo)