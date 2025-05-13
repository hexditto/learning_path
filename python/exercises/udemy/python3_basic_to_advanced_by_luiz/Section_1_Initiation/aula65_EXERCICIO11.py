"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_usuario = input("Digite o seu CPF: ")
checador_numero = None
cpf_string = ''
faixa_primeiro_digito = range(0,9)
faixa_segundo_digito = range(0, 10)
ultimos_digitos = cpf_usuario[-2::]
decrescente_1 = list(range(10, 1, -1))
decrescente_2 = list(range(11, 1, -1))
soma_1 = 0
soma_2 = 0
resultado_primeiro_digito = 0
resultado_segundo_digito = 0

# Conversão da entrada do usuário em uma string
for digito in cpf_usuario:
    checador_numero = digito.isnumeric()
    if checador_numero:
        cpf_string += digito
    else:
        continue


# Cálculo do primeiro dígito
for i in faixa_primeiro_digito:
    soma_1 += int(cpf_string[i]) * decrescente_1[i]

resultado_primeiro_digito = (soma_1 * 10) % 11
resultado_primeiro_digito = resultado_primeiro_digito \
    if resultado_primeiro_digito <= 9 else 0

# Cálculo do segundo dígito
for j in faixa_segundo_digito:
    soma_2 += int(cpf_string[j]) * decrescente_2[j]

resultado_segundo_digito = (soma_2 * 10) % 11
resultado_segundo_digito = resultado_segundo_digito \
    if resultado_segundo_digito <= 9 else 0


# Bloco de avaliação do CPF
cpf_calculado = f"{cpf_string[:9]}{resultado_primeiro_digito}{resultado_segundo_digito}"

if cpf_usuario == cpf_calculado:
    print(f"{cpf_usuario} é válido!")
else:
    print(f"{cpf_usuario} NÃO é válido!")
