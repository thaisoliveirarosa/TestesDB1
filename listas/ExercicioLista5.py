# Escreva um programa que conte quantas string tenham tamanho maior que 2 e o primeiro e último caracteres sejam iguais.
# (Exemplo de lista: ['abc', 'xyz', 'aba', '1221']) (Resultado esperado: 2)

lista = ['abc', 'xyz', 'aba', '1221']
numeroStrings = 0

for string in lista:
    if len(string) > 2 and string[0] == string[-1]:
        numeroStrings += 1

print("Existem", numeroStrings, "strings na lista que possuem tamanho maior que 2 e o primeiro e último caracteres iguais.")
