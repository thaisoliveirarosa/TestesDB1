# Faça um programa para a leitura de duas notas parciais de um aluno.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

nota = (n1 + n2) / 2

if nota >= 7 and nota <= 10:
    print('Você foi aprovado!')
elif nota > 10:
    print('Média inválida.')
else:
    print('Você foi reprovado.')