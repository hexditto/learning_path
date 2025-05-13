###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Cupons de Desconto I
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

# Leitura de dados


# Cálculo da melhor atribuição de cupons


# Impressão da resposta

x1_reais_desconto = 15
z1_compras_acima_de = 85
x2_porcentagem_de_desconto = 15
z2_limite_reais = 25
x3_porcentagem_de_desconto = 5
z3_compras_acima_de = 90
numero_de_compras_semanais = 9
compras = {1:180, 2:190, 3:120, 4:100, 5:30, 6:90, 7:120, 8:40, 9:130}
#compras = {1: 90, 2: 130, 3: 10, 4: 20, 5: 190, 6: 80, 7: 60, 8: 40}
desconto_1 = []
desconto_2 = []
desconto_3 = []

# Cálculo Cupom 1
for i, j in compras.items():
    if j > z1_compras_acima_de:
        tupla_1 = (i, x1_reais_desconto)
        desconto_1.append(tupla_1)
    else:
        tupla_1 = (i, 0)
        desconto_1.append(tupla_1)
        continue


# Cálculo Cupom 2
for i, j in compras.items():
    calc_2 = j * (x2_porcentagem_de_desconto / 100)
    if calc_2 > z2_limite_reais:
        tupla_2 = (i, z2_limite_reais)
        desconto_2.append(tupla_2)
    else:
        tupla_2 = (i, calc_2)
        desconto_2.append(tupla_2)

# Cálculo Cupom 3
for i, j in compras.items():
    if j > z3_compras_acima_de:
        calc_3 = j * (x3_porcentagem_de_desconto / 100)
        tupla_3 = (i, calc_3)
        desconto_3.append(tupla_3)
    else:
        tupla_3 = (i, 0)
        desconto_3.append(tupla_3)
        continue

print(desconto_1)
print(desconto_2)
print(desconto_3)

# Exemplo monitoria
for x in range(numero_de_compras_semanais):
    for y in range(numero_de_compras_semanais)
        if y != x:
        for z in range(numero_de_compras_semanais)
            if z != y and z != x:
