# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o 
# valor da variável

def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

lista_de_numeros = 1, 2, 3, 4, 5
variavel = multiplicador(*lista_de_numeros)
print(variavel)

# Crie uma função que fale se um número é par
# ou ímpar. Retorne se o número é par ou ímpar.

def par_impar(x=None):
    if x is None:
        return "Entrada inválida"
    conversor = int(x)
    avaliador = conversor % 2
    if not avaliador:
        return f"O número {x} é par!"
    return f"O número {x} é ímpar"

coletador = par_impar(2)
print(coletador)

coletador = par_impar(3)
print(coletador)

coletador = par_impar(7)
print(coletador)

coletador = par_impar(0)
print(coletador)

coletador = par_impar(-300)
print(coletador)


