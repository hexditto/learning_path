"""
Introdução ao desempacotamento
"""

# nomes = ["Maria", "Helena", "Luiz"]
# nome1, nome2, nome3 = nomes
# print(nome2)

# *resto ou *_ pega todos os outros valores que não
# foram relacionados em uma variável e formam um
# pacote
_, _, nome, *resto = ["Maria", "Helena", "Luiz"]
print(nome, resto)