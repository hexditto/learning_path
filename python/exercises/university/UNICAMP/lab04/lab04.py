###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Picos e Vales I
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

# Leitura e iniciação dos dados
dados = []
picos = 0
vales = 0
contador = 2


# Formação da lista
for valores in range(0, 100):
    dados.append(int(input()))
    if dados[-1] == 0:
        dados.pop(-1)
        break


# Looping para interpretação da lista
for x in dados [1::]:
    if contador != len(dados): # Evitar erro de index da lista
        if x > dados[contador] and x > dados [-len(dados) + (contador - 2)]: # Análise de pico (dado anterior e posterior)
            picos += 1
        elif x < dados[contador] and x < dados [-len(dados) + (contador - 2)]: # Análise de vale (dado anterior e posterior)
            vales += 1
        contador += 1
    else:
        break


# Resultado
print('Quantidade de picos:', picos)
print('Quantidade de vales:', vales)
