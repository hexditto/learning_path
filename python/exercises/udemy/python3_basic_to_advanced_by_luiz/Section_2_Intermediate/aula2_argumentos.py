"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


        # Parâmetros
def soma(x, y, z):
    # Definição
    print(f"{x=} + {y=} + {z=}", "|", "x + y + z = ", x + y + z)

# Argumentos são os valores na função
soma(1, 2, 3) # Argumento posicional
soma(1, y=2, z=5) # Argumentos nomeados

print(1, 2, 3, sep="-")