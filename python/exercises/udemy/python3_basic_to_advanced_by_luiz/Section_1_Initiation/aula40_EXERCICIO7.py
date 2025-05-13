"""
Calculadora com While
"""

while True:
    saida = input("Deseja utilizar a calculadora? \
                  [s]im ou [n]ao \
                  ")
    positivo = saida.lower().startswith('s') # Caso não seja sim
    if not positivo:
        break
    num_1_float = 0
    num_2_float = 0
    tamanho_operador = 0
    numeros_validos = None # Flag
    operacoes_permitidas = '+-*/'
    try:
        numero_1 = input("Digite o primeiro número: ")
        numero_2 = input("Digite o segundo número: ")
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True 

    except:
        numeros_validos = None
    if numeros_validos is None:
        print("Um ou mais números digitados inválidos!")
        continue
    
    operador = input("Digite qual operador utilizar [+-/*]: ")

    if operador not in operacoes_permitidas:
        print("Operador inválido!")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue
    

    if operador == "+":
        operacao = num_1_float + num_2_float
    elif operador == "-":
        operacao = num_1_float - num_2_float
    elif operador == "*":
        operacao = num_1_float * num_2_float
    elif operador == "/":
        operacao = num_1_float / num_2_float
    else:
        print("Apenas utilizar dentre: '+', '-', \
              '*', '/'")
    print(f'{num_1_float} {operador} {num_2_float} = {operacao}')
