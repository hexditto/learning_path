"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com erros
de índices inexistentes na lista.
"""

import os

# Variáveis
lista = []
opcoes = ['i', 'a', 'l', 's']
avaliador = None
digito = None
mercadoria = ''

while True:
    escolha_usuario = input(f"Selecione uma opção:\n"\
                            f"[i]nserir [a]pagar [l]istar [s]air: ")
    avaliador = escolha_usuario in opcoes
    if not avaliador: # Avalia se o usuário escolheu as opções dispostas
        print("Entrada inválida!")
        continue

    if escolha_usuario == 'i': # Bloco da adição na lista
        os.system("clear")
        mercadoria = input("Mercadoria: ")
        lista.append(mercadoria)

    elif escolha_usuario == 'a': # Bloco da remoção da lista
        os.system("clear")
        if len(lista) == 0: # Caso a lista já esteja vazia
            print("Não há nada para apagar")
            continue
        for indice, nome in enumerate(lista):
            print(indice, nome)
        indice_usuario = input("Escolha um índice: ")
        if len(indice_usuario) > 1:
            print("Digite apenas um dígito")
            continue
        digito = indice_usuario.isnumeric() # Avaliar se o usuário digitou um número
        if not digito:
            print("Digite apenas números.")
            continue
        indice_usuario = int(indice_usuario)

        if indice_usuario < 0 and indice_usuario > indice:
            print("Índice inválido!")
        del lista[indice_usuario]

    elif escolha_usuario == 'l': # Bloco para dispor a lista já feita
        os.system("clear")
        if lista == []:
            print("A lista está vázia.")
            continue
        for indice, nome in enumerate(lista):
            print(indice, nome)

    elif escolha_usuario == 's': # Bloco para sair do sistema
        os.system("clear")
        if lista != []:
            print("Obrigado pela utilização do sistema!\n"\
                "Lista Final:\n")
            for indice, nome in enumerate(lista):
                print(indice, nome)
        else:
            print("Até mais!")
        break