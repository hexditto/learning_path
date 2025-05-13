###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Classificação de Imagens
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

# Leitura de dados

quantidade_de_dados = int(input())
lista_geral_animais = [input().split() for i in range(quantidade_de_dados)]
animais_database = {}
animais_mais_repetidos = []

# Iteração na lista de listas
for listas in (lista_geral_animais):
    for palavras in listas:
        if palavras in animais_database.keys(): # Geração do dicionário
            animais_database[palavras] += 1
        else:
            animais_database[palavras] = 1

# Comparação da quantidade de cada animal com a quantidade de modelos gerados
for animal, valor in animais_database.items(): 
    if (valor / quantidade_de_dados) >= 0.5: # Determinação dos animais mais repetidos
        animais_mais_repetidos.append(animal)

# Bloco de organização da resposta final
if len(animais_mais_repetidos) > 0:
    animais_mais_repetidos.sort()
    print('Animais preditos: ', end='')
    print(*animais_mais_repetidos[::], sep= ', ')
else:
    print('Nenhum animal foi predito')

