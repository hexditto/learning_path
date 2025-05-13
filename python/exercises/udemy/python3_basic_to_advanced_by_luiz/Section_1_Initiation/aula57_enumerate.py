"""
for in com listas
[(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
"""

lista = ["Maria", "Helena", "Luiz"]
lista.append("João")

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)
# lista_enumerada = list(enumerate(lista, start= 23))
# print(lista_enumerada)

for indice, nome in enumerate(lista):
    print(indice, nome)