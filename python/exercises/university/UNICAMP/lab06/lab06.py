###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Picos e Vales II
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

# Leitura das amostras
terreno_1 = [int(i) for i in input().split()]
terreno_2 = [int(i) for i in input().split()]
interpretacao_1 = []
interpretacao_2 = []
picos = 0
vales = 0
contador_1 = 0
contador_2 = 0


# Looping para interpretação das listas de terrenos
for x in terreno_1 [1:-1:]:
    if contador_1 != len(terreno_1): # Contador percorre toda a lista
        if x > terreno_1[contador_1] and x > terreno_1[(2+contador_1)]: # Análise de pico (dado anterior e posterior)
            picos += 1
            interpretacao_1.append('p') # Adição de um pico na lista de terreno 1
        elif x < terreno_1[contador_1] and x < terreno_1 [(2+contador_1)]: # Análise de vale (dado anterior e posterior)
            vales += 1
            interpretacao_1.append('v') # Adição de um vale na lista de terreno 1
        contador_1 += 1
    else:
        break

for y in terreno_2 [1:-1:]: # Mesma lógica para o terreno 2
    if contador_2 != len(terreno_2):
        if y > terreno_2[contador_2] and y > terreno_2[2+contador_2]:
            interpretacao_2.append('p')
        if y < terreno_2[contador_2] and y < terreno_2[2+contador_2]:
            interpretacao_2.append('v')
        contador_2 += 1
    else:
        break

if len(interpretacao_1) == len(interpretacao_2): # Caso o número de casos entre os dois sejam iguais
    if interpretacao_1 == interpretacao_2: # Caso seja a mesma lista
      print("As sequências e as quantidades de picos e vales são iguais")
    else:
      print("As quantidades de picos e vales são iguais")
else:
  print("As sequências e as quantidades de picos e vales são diferentes")