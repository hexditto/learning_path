# IMC = peso / (altura x altura)
nome = 'Henrique Dias'
altura = 1.73
peso = 65
imc = peso / (altura ** 2) 
dinheiro = 10003121.5 # Casas decimais

# f-strings (formatação de strings)

print(f'O índice de IMC é {imc:.3f}\n')

print(f'{nome} tem {altura:.2f} de altura, \n pesa {peso} quilos e seu imc é, \n {imc:.2f}')

print(f'Exemplo de fstring manipulando dinheiro {dinheiro:,.2f}')
print(dinheiro)