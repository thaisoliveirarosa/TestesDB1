# Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = input('Escreva um número: ')
b = input('Escreva um número: ')
c = input('Escreva um número: ')

if a >= b >= c and a >= c:
    print(f'A ordem decrescente é {a} , {b} e {c}')
elif a >= b and a >= c >= b:
    print(f'A ordem decrescente é {a} , {c} e {b}')
elif b >= a >= c and b >= c:
    print(f'A ordem decrescente é {b} , {a} e {c}')
elif b >= a and b >= c >= a:
    print(f'A ordem decrescente é {b} , {c} e {a}')
elif c >= a >= b and c >= b:
    print(f'A ordem decrescente é {c} , {a} e {b}')
elif c >= a and c >= b >= a:
    print(f'A ordem decrescente é {c} , {b} e {a}')