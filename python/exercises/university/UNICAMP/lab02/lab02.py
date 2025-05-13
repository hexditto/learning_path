###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Trem das Onze
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

# Dados do trem:
_tremHora = 11
_tremMin = 0

# Dados do ônibus 1:
_busHora1 = int(input(f'Qual é a hora do primeiro ônibus (h)? '))
_busMin1 = int(input(f'Quais são os minutos do primeiro ônibus (min)? '))
_busDist1 = int(input(f'Qual a distância a ser percorrida pelo primeiro ônibus (km)? '))
_busVeloc1 = int(input(f'Qual a velocidade do primeiro ônibus (km/h)? '))

# Dados do ônibus 2:
_busPrimeiraHora2 = int(input(f'Qual é a hora do segundo ônibus (h)? '))
_busPrimeiroMin2 = int(input(f'Quais são os minutos do segundo ônibus (min)? '))
_busDist2 = int(input(f'Qual a distância a ser percorrida pelo segundo ônibus (km)? '))
_busVeloc2 = int(input(f'Qual a velocidade do segundo ônibus (km/h)? '))

print(f'Horário primeiro ônibus: {_busHora1} horas e {_busMin1} minutos.')
print(f'Horário segundo ônibus {_busPrimeiraHora2} horas e {_busPrimeiroMin2} minutos.')

# Cálculo do tempo de percurso do ônibus 1:
_busTempo1 = round(((_busDist1 / _busVeloc1) * 60))
_novoMin1 = _busMin1 + _busTempo1
print(f'O primeiro ônibus irá demorar {_busTempo1} minutos.')

# Cálculo do tempo de percurso do ônibus 2:
_busTempo2 = round((_busDist2 / _busVeloc2) * 60)
_novoMin2 = _busPrimeiroMin2 + _busTempo2
print(f'O segundo ônibus irá demorar {_busTempo2} minutos.')

# Conversão e ajuste do tempo adicional do ônibus 1:
if _novoMin1 >= 60:
    _busHora1 += 1
    _novoMin1 -= 60
    print(f'O primeiro ônibus chegará ao destino às {_busHora1} horas e {_novoMin1} minutos')

else:
    print(f'O primeiro ônibus chegará ao destino às {_busHora1} horas e {_novoMin1} minutos')

# Conversão e ajuste do tempo adicional do ônibus 2:
if _novoMin2 >= 60:
    _novaHora2 = _busPrimeiraHora2 + 1
    _novoMin2 = _novoMin2 - 60
    print(f'O segundo ônibus chegará ao destino às {_novaHora2} horas e {_novoMin2} minutos')

else:
    print(f'O segundo ônibus chegará ao destino às {_busPrimeiraHora2} horas e {_novoMin2} minutos')
    _novaHora2 = _busPrimeiraHora2

# Bloco de código dos ônibus e trens:
if _busHora1 < _busPrimeiraHora2:
    if _novaHora2 < _tremHora:
        print(_novaHora2 < _tremHora)
    else:
        print(_novaHora2 < _tremHora)
elif _busHora1 == _busPrimeiraHora2 and _novoMin1 < _busPrimeiroMin2:
        if _novaHora2 < _tremHora:
            print(_novaHora2 < _tremHora)
        else:
            print(_novaHora2 < _tremHora)
else:
    print(_busHora1 < _busPrimeiraHora2)