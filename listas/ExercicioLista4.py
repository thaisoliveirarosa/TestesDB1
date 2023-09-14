# Escreva um programa que conte o número de caracteres de uma string
# Exemplo: 'google.com'
# Resultado Esperado: {'o' : 3, 'g' : 2, '.' : 1, 'e' : 1, 'l' : 1, 'm' : 1, 'c' : 1}

string = 'google.com'
caracteres = {}

for letra in string:
    if letra in caracteres:
        caracteres[letra] += 1
    else:
        caracteres[letra] = 1

print(caracteres)


