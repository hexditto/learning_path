###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - A Caçada II
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

'''
Função recursiva para simular o caminho do gato. A função recebe
uma matriz representando as plataformas e a posição (linha,coluna)
do gato. A função deve retornar o número máximo de petiscos recolhidos.
'''
def simula_caminho(plataformas, linha, coluna, direcao):
    if linha < 0 or linha >= len(plataformas) or coluna < 0 or coluna >= len(plataformas[linha]):
        return 0, []

    if plataformas[linha][coluna] == '.':
        return 0, []

    if plataformas[linha][coluna] == '*':
        petisco = 1
    else:
        petisco = 0

    plataformas[linha][coluna] = '.'  # Marca o local como visitado

    if coluna == 0 and direcao == -1:
        # O gato chegou à fronteira esquerda, muda a direção para direita
        direcao = 1
    elif coluna == len(plataformas[linha]) - 1 and direcao == 1:
        # O gato chegou à fronteira direita, muda a direção para esquerda
        direcao = -1

    # Tenta cair para o nível de baixo na mesma coluna
    petisco1, caminho1 = simula_caminho(plataformas, linha + 1, coluna, direcao)

    # Tenta continuar no mesmo nível na nova direção
    petisco2, caminho2 = simula_caminho(plataformas, linha, coluna + direcao, direcao)

    # Verifica qual caminho tem o maior número de petiscos
    if petisco1 >= petisco2:
        petisco += petisco1
        caminho = [(linha, coluna)] + caminho1
    else:
        petisco += petisco2
        caminho = [(linha, coluna)] + caminho2

    # Marca o local como não visitado para outras simulações
    plataformas[linha][coluna] = '*' if petisco > 0 else '_'

    return petisco, caminho


plataformas = []
n = int(input())

for i in range(n):
    plataformas.append(list(input()))

resultado, caminho = simula_caminho(plataformas, 0, 0, 1) 
print(resultado)
