"""
Iterando strings com while
"""
#       012345678910
nome = "Henrique Dias" # Iteráveis
#     1110987654321

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
nova_string = ''
indice = 0

while indice < tamanho_nome:
    letra = nome[indice]
    nova_string += '*' + letra
    print(f'{nova_string=}')
    indice += 1

print(nova_string)