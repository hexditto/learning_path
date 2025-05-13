#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Carrinho Elétrico
# Nome: Henrique Dias Benedicto
# RA: 174535
#####################################################



# Função que cria uma pista de corrida, com extremidades completadas com '#'
def circuito_do_carro(n, m):
  circuito = []
  extremo_superior = ['#'] * (m + 2)
  extremo_inferior = ['#'] * (m + 2)
  circuito.append(extremo_superior)
  for i in range(n):
    i = ['#'] + input().split() +['#']
    circuito.append(i)
  circuito.append(extremo_inferior)
  return circuito

# Leitura do circuito
n, m = [int(i) for i in input().split()]
voltas = 0
direcoes = []
carrinho = ''
pista = circuito_do_carro(n, m)

# Formação de uma lista de direções
for x in range(60):
  a = input()
  if a != '0':
    direcoes.append(a.split())
  else:
    break

# Método para achar o ponto inicial do circuito
for i in range(len(pista)):
  for j in range(len(pista[0])):
    if pista[i][j] == '-':
      carrinho = pista[i][j] # Guarda a informação de posição
      linha = i
      coluna = j

# Iteração nas direções para movimentar o carrinho
for comandos in direcoes:
  if comandos[1] == 'N':
    for n in range(int(comandos[0])): # Move o carrinho em direção norte 'n' vezes
      linha -= 1
      if pista[linha][coluna] == '#': # Mantém-se parado ao encontrar uma barreira
        linha += 1
      else:
        carrinho = pista[linha][coluna] 
        if carrinho == '-': # Adiciona uma volta caso o carrinho retorne ao ponto inicial
          voltas += 1
  elif comandos[1] == 'S': # Move o carrinho em direção sul 's' vezes
    for s in range(int(comandos[0])):
      linha += 1
      if pista[linha][coluna] == '#': # Mantém-se parado ao encontrar uma barreira
        linha -= 1
      else:
        carrinho = pista[linha][coluna]
        if carrinho == '-': # Adiciona uma volta caso o carrinho retorne ao ponto inicial
          voltas += 1    
  elif comandos[1] == 'L': # Move o carrinho em direção lesta 'l' vezes
    for l in range(int(comandos[0])):
      coluna += 1
      if pista[linha][coluna] == '#': # Mantém-se parado ao encontrar uma barreira
        coluna -= 1
      else:
        carrinho = pista[linha][coluna]
        if carrinho == '-': # Adiciona uma volta caso o carrinho retorne ao ponto inicial
          voltas += 1
  elif comandos[1] == 'O': # Move o carrinho em direção oeste 'o' vezes
    for o in range(int(comandos[0])):
      coluna -= 1
      if pista[linha][coluna] == '#': # Mantém-se parado ao encontrar uma barreira
        coluna += 1
      else:
        carrinho = pista[linha][coluna]
        if carrinho == '-': # Adiciona uma volta caso o carrinho retorne ao ponto inicial
          voltas += 1

# Impressão da saída
print('Voltas completadas:', voltas)
