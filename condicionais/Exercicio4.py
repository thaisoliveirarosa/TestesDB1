# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra: '))

if (letra in ('aeiou') or letra in ('AEIOU')):
    print('Vogal')
elif (letra.isnumeric()):
    print('Número')
else:
    print('Consoante')