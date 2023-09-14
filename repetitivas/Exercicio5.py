# Faça um Programa que leia três números e mostre o maior deles.

menor = 0
maior = 0

for n in range(1, 4):
    numeroAtual = int(input('Digite o ' + str(n) + 'º número: '))
    if menor == 0:
        menor = numeroAtual
    if numeroAtual < menor:
        menor = numeroAtual
    if maior < numeroAtual:
        maior = numeroAtual

print('O maior é:', maior, ' e o menor é:', menor)
