###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Novos Algoritmos de Ordenação
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

def selecao_e_insercao(lista):
    trocas = 0
    for i in range(len(lista)):
        minimo = min(lista[i:])
        if lista[i] > minimo:
            j = lista.index(minimo, i)
            while j > i:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                j -= 1
                trocas += 1
            print(lista)
        if lista ==  sorted(lista):
            break
    return trocas

def bubble_sort_adaptado(lista):
    n = len(lista)
    trocas = 0
    comeco = 0
    final = n - 1 
    averiguador = True

    while averiguador:
        averiguador = False
 
        for k in range(comeco, final):
            if lista[k] > lista[k + 1]:
                lista[k], lista[k + 1] = lista[k + 1], lista[k]
                trocas += 1
                averiguador = True
        print(lista)
        if not averiguador:
            break
        

        averiguador = False
        final -= 1
  
        for j in range(final - 1, comeco - 1, -1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
                averiguador = True
        comeco += 1
        if lista != sorted(lista):
            print(lista)
    return trocas

# Leitura da sequência
lista = [int(a) for a in input().split()]
lista2 = lista[::]
lista3 = lista[::]

# Execução dos algoritmos de ordenação e impressão dos resultados
print("Algoritmo Seleção e Inserção:")
X = selecao_e_insercao(lista2)
print("Trocas realizadas:", X)
print()
print("Algoritmo Bubble Up and Down:")
Y = bubble_sort_adaptado(lista3)
print('Trocas realizadas:', Y)
# print("Trocas realizadas:", Y)
