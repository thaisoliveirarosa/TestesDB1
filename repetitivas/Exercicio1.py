# Faça um Programa que peça dois números e imprima a soma.

soma = 0

for vez in range(1, 3):
    soma = soma + int(input('Escreva o ' + str(vez) + 'º número: '))

print('A soma dos dois números é', soma)