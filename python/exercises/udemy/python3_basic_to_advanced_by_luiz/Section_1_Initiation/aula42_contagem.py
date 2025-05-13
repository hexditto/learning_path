# Contagem de quantas vezes uma letra_atual apareceu
# Qual foi a letra_atual que apareceu mais?

frase = "O Python é uma linguagem de programação " \
        "multiparadigma. " \
        "Python foi criado por Guido van Rossum."
print(frase)

tamanho = len(frase)
print(tamanho)
i = 0
contagem = 0
letra_mais_repetida = ''

while i < tamanho:
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    quantidade = frase.count(letra_atual)
    if quantidade > contagem:
        contagem = quantidade
        letra_mais_repetida = letra_atual
    i += 1
print(f"A letra '{letra_mais_repetida}' repetiu {contagem} vezes")