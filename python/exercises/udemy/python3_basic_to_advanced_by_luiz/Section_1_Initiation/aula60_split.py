"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = "    Olha só que,    coisa interessante   "
lista_palavras_cruas = frase.split(', ')
lista_palavras_fixed = []

for i, frase in enumerate(lista_palavras_cruas):
    lista_palavras_fixed.append(lista_palavras_cruas[i].strip())

# print(lista_palavras_cruas)
# print(lista_palavras_fixed)

frases_unidas = '-'.join('abc')
print(frases_unidas)
frases_unidas = ', '.join(lista_palavras_fixed)
print(frases_unidas)