###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Qual o Melhor Cartão de Crédito?
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

# Listas para os dados
cartao_cashback = []
cartao_milhas = []
escolha_cartão = []
faturas = []

# Zona de input do usuário
taxa_de_anuidade_cartao_cash = int(input())
taxa_de_anuidade_cartao_milhas = int(input())
valor_de_conversao_milhas_reais = int(input())
preco_da_passagem_em_reais = int(input())
preco_da_passagem_em_milhas = int(input())

# Criação de lista de fatura
for x in range(0, 12):
    a = int(input())
    faturas.append(a)
    

def calculo_cashback(valor):
    """Calcula o cashback em 1%"""
    retorno = (0.01 * valor)
    return retorno


def calculo_milhas(valor):
    """Calcula as milhas da passagem"""
    milha = int(valor / 5)
    return milha


# Geração das listas de benefícios cashback e milhas
for valores in faturas:
    beneficio_cash = calculo_cashback(valores)
    cartao_cashback.append(beneficio_cash)
    beneficio_milhas = calculo_milhas(valores)
    cartao_milhas.append(beneficio_milhas)

# Despesas prováveis
despesa_gratuito = 0 + preco_da_passagem_em_reais - 0
despesa_cash = taxa_de_anuidade_cartao_cash + preco_da_passagem_em_reais - sum(cartao_cashback)
despesa_milhas = taxa_de_anuidade_cartao_milhas + preco_da_passagem_em_reais - ((sum(cartao_milhas) // 1000) * valor_de_conversao_milhas_reais)


# Avaliação da utilização de milhas ou reais
if sum(cartao_milhas) < preco_da_passagem_em_milhas:
    escolha_cartão = dict({ # Criação de um dicionário para escolher o melhor cartão
        despesa_gratuito: 'Cartão Gratuito',
        despesa_cash: 'Cartão Cashback',
        despesa_milhas: 'Cartão Milhas'
                        })
    dicionario_ajeitado = sorted(escolha_cartão)
    MELHOR_CARTAO = escolha_cartão.get(dicionario_ajeitado[0])
else:
    despesa_milhas = taxa_de_anuidade_cartao_milhas - (((sum(cartao_milhas) - preco_da_passagem_em_milhas) // 1000) * valor_de_conversao_milhas_reais)  #print('Escolhi as milhas')
    MELHOR_CARTAO = 'Cartão Milhas'


# Impressão da resposta

print("Cartão Gratuito: {:.2f}".format(despesa_gratuito))
print("Cartão Cashback: {:.2f}".format(despesa_cash))
print("Cartão Milhas: {:.2f}".format(despesa_milhas))

print(MELHOR_CARTAO)
