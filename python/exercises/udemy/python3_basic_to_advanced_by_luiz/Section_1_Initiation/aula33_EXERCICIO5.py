"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número inteiro: ")

try:
    numero_inteiro = numero.isdigit()
    if numero_inteiro:
        calc_numero_par = int(numero) % 2
        if calc_numero_par == 0:
            print("Número par")
        else:
            print("Número ímpar")
    else:
        print("Não é um número inteiro")
except:
    print("Por favor, digite um número")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input("Qual a hora? ")

try:
    hora = int(horario)
    manha = hora >= 0 and hora <= 11
    tarde = hora >= 12 and hora <= 17

    if manha:
        print("Bom dia!")
    elif tarde:
        print("Boa tarde!")
    else:
        print("Boa noite!")

except:
    print("Por favor, digite apenas números inteiros")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input("Digite o seu primeiro nome: ")

try:
    tamanho_nome = len(primeiro_nome)
    curto = tamanho_nome <= 4
    médio = tamanho_nome >= 5 and tamanho_nome <= 6

    if curto:
        print("Seu nome é curto")
    elif médio:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
except:
    print("Deu erroo")