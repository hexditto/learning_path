"""
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
= Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0 > -100,.1f
Conversion flags - !r !s !a
"""
variavel = "ABCDEF"
print(f'{variavel}')
print(f'{variavel:x>10}') # Adicionar 10 espaços à esquerda
print(f'{variavel:x<10}.') # Adicionar 10 espaços à direita
print(f'{variavel:x^10}.') # Adicionar ao centro com 10 espaços totais
print(f'{1000.294914281247193:+.1f}') # Casas decimais
print(f'{-1000.294914281247193:+.1f}') # Casas decimais 
print(f'{-1000.294914281247193:0=+10,.1f}') # Com igual

print(f'O hexadecimal de 1500 é {1500:08X}') # Hexadecimal
