# Faça um Programa que peça dois números e imprima o maior deles.

contador = 0
numero = 0

while contador < 2:
    contador = contador + 1
    numeroAtual = input('Digite um número: ')
    if int(numero) < int(numeroAtual):
        numero = numeroAtual

print('O número maior é:', numero)