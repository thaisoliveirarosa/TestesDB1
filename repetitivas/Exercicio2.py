# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

somaNotas = 0
contador = 0

while contador < 4:
    contador = contador + 1
    somaNotas = somaNotas + float(input('Escreva a nota do ' + str(contador) + 'º bimestre: '))

media = somaNotas / contador

print('A sua média é', media)
