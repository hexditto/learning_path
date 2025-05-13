"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear,
extend, +
Create, Read, Update, Delete (CRUD)
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
# lista[2] = 300
# del lista[2] # Del remove um item e move toda a lista => cuidado com processamento
# print(lista)
# print(lista[2])
lista.append(70) # Adicionar ao final da lista
lista.append(80)
lista.append(90)
print(lista)
lista.pop() # Retira o ultimo lista da lista
print(lista)
ultimo_valor = lista.pop()
print(lista, "Removido", ultimo_valor)