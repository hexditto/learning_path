###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Tradutor de Código Morse
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

# Formação de um dicionário

morse_dic = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}

def tradutor_morse(texto_morse):
    ''' Função que separa, analisa e traduz uma string de código morse'''
    # Gerar lista da string e criar listas vazias
    separacao_morse = texto_morse.split(' ')
    letras_morse = []
    letras_possiveis = []
    for separados in separacao_morse: # Iterar em cada código morse
        if separados.endswith('*'): # Análise do código morse com erro
            for morse, letras in morse_dic.items():
                if morse.startswith(separados[:-1]):
                    # Separa todos os códigos com pontos e vírgulas até o *
                    letras_possiveis.append(letras)
                    letras_possiveis.sort # Ordem alfabética
            possibilidades = '[' + ''.join(letras_possiveis) + ']'
            letras_morse.append(possibilidades)
            letras_possiveis = []
        elif separados == '':
            letras_morse.append(' ')
        else:
            letras_morse.append(morse_dic.get(separados, ' '))
    return ''.join(letras_morse) # Retorna uma string feita pelas listas


morse_str = input()
coletor = tradutor_morse(morse_str)
print(coletor)