###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - A Caçada I
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################


plataformas = []
n = int(input())

for i in range(n):
  plataformas.append(list(input()))
nulo = [0] * len(plataformas[0])
plataformas.append(nulo)


i = 0
j = 0
voltas = 0
direcao = 1
petiscos_coletados = 0

while True:
  gatinho = plataformas[i][j]
  if gatinho == '*':
    petiscos_coletados += 1
    plataformas[i][j] = 'x'
  elif gatinho == '.':
    i += 1
    continue

  if j == len(plataformas[0]) - 1:
    direcao = -1
    voltas += 1
  elif j == 0 and direcao == -1:
    direcao = 1
    voltas += 1
  j += direcao


  if gatinho == 0:
    break
  if voltas > 10:
    break
  

print(petiscos_coletados)

