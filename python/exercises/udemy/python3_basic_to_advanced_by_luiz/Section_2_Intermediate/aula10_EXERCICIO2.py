# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def create_multiple(multiplier):
    def multiplicate(number):
        return number * multiplier
    return multiplicate # Deixa engatada a função

triplicate = create_multiple(3) # Criou uma função triplicar

for numbers in [1, 4, 6, 7]:
    result = triplicate(numbers) # Numbers é o parametro da linha 6
    print(result)
        