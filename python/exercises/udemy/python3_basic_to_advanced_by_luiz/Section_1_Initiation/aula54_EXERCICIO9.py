"""
for in com listas
"""

lista = ["Maria", "Helena", "Luiz"]
lista.append("João")
indices = range(len(lista))

for i in indices:
    print(i, lista[i], type(lista[i]))