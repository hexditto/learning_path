"""
Faça um jogo para o usuário adivinhar qual a 
palavra secreta.
- Vocẽ vai propor uma palavra secreta qualuqer
e vai dar a possibilidade para o usuário
digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está na palavra
secreta.
    - Se a letra digitada estiver na palavra
    secreta; exiba a letra;
    - Se a letra digitada não estiver na
    palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

# palavra_secreta = 'coelho'
# avaliador = None
# digito = None
# tentativas = 0
# print("Jogo da palavra secreta!")
# colhedor_de_letras = ''
# lixo = ''
# entrada = ''

# while True:
    # if len(colhedor_de_letras) ==  len(palavra_secreta):
    #     print("Acabou!")
    #     break
#     entrada = input("Digite uma letra: ")
#     digito = entrada.isdigit()
    # avaliador = True
    # if digito:
    #     print("Letra inválida!")
    #     continue
    # if len(entrada) > 1:
    #     print("Digite apenas uma letra.")
    #     continue
#     if entrada in palavra_secreta:
#         colhedor_de_letras += entrada
#         tentativas += 1
#         print(f"{entrada} é uma letra na palavra" \
#               f"secreta. {colhedor_de_letras=}")
#         continue
#     else:
#         lixo += entrada
#         tentativas += 1
#         print(f"Letra não está na palavra."\
#               f"{lixo=}")
#         continue

import os

palavra = 'coelho'
tamanho_palavra = len(palavra)
quantidade_letra = 0
checador = None
digito = None
misterio = '******'
colhedor = ''
tentativas = 0

print(f"Bem-vind@ ao jogo!\n Descubra a palavra misteriosa!\n {misterio}")

while True:
    letra_usuário = input("Digite uma letra: ")
    digito = letra_usuário.isdigit()
    if digito:
        print(f"Letra inválida!")
        continue
    if len(letra_usuário) > 1:
        print(f"Digite apenas uma letra.")
        continue
    quantidade_letra = palavra.count(letra_usuário)
    checador = bool(quantidade_letra)
    if checador:
        for i in range(tamanho_palavra):
            if letra_usuário == palavra[i] and misterio[i] == "*":
                colhedor += palavra[i]
            elif misterio[i] != '*':
                colhedor += misterio[i]
            else:
                colhedor += '*'
        misterio = colhedor
        colhedor = ''
        tentativas += 1
        print(f"{misterio}. Tentativas = {tentativas}")

    else:
        tentativas += 1
        print(f"Palavra não encontrada. Tentativas = {tentativas}")
    if misterio.count("*") == 0:
        os.system("clear")
        print(f"PARABÉNS, VOCÊ GANHOU. \nTentativas = {tentativas}. \nPalavra = {misterio}")
        break