###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Chuva de Meteoritos
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

def area_fazenda(n, m): # Criação da Fazenda
  fazenda = []
  for i in range(n):
    linha_fazenda = []
    for zonas in range(m):
      linha_fazenda = [0] * m
    fazenda.append(linha_fazenda)
  return fazenda


dados_fazenda = input().split()
fazenda = area_fazenda(int(dados_fazenda[0]), int(dados_fazenda[1])) # linha_fazenda, coluna_fazenda
numero_de_meteorito = int(input())


for vezes in range(numero_de_meteorito): # Iterar para cada meteorito
    linha_meteorito, coluna_meteorito, raio_meteorito = [int(i) for i in input().split()] # 
    for linha_fazenda in range(linha_meteorito - raio_meteorito + 1, linha_meteorito + raio_meteorito):
        if linha_fazenda < len(fazenda) and linha_fazenda >= 0:
            for coluna_fazenda in range(coluna_meteorito - raio_meteorito + 1, coluna_meteorito + raio_meteorito):
                if coluna_fazenda < len(fazenda[0]) and coluna_fazenda >= 0:
                    fazenda[linha_fazenda][coluna_fazenda] += 1
   
for zonas in fazenda:
    print(*zonas)            

