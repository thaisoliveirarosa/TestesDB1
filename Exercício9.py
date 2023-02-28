# Faça um programa que pergunte em que turno você estuda

turno: str = input('Em qual turno você estuda? M - Matutino, V - Vespertino, N - Noturno: ')

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido')
