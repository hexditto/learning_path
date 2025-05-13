###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Escolha da Missão
# Nome: Henrique Dias Benedicto
# RA: 174535
###################################################

# Leitura de dados
_nivelPersonagem = int(input())
_ataque = int(input())
_defesa = int(input())
_moedas = int(input())
_missao = 0
_recompensaMissao1 = 25
_recompensaMissao2 = 40
_recompensaMissao3 = 100
_recompensaMissao4 = 40
_recompensaMissao5 = 130
_recompensaMissao6 = 30

# Escolha da missão
if _nivelPersonagem >= 5: # começar pelo missao 6 e 5
    if _defesa >= 50 and _moedas >= 0:
        if _ataque >= 40 and _moedas >= 50:
            _moedas += _recompensaMissao5 - 50
            _missao = 5
        elif _ataque >= 50:
            _moedas += (_recompensaMissao6) * 2
            _missao = 6
        elif _defesa >= 50:
            _moedas += _recompensaMissao6
            _missao = 6

elif _nivelPersonagem >= 3: # missões 3, 4, 6, 1 e 2
    if _ataque < _defesa and _moedas >= 50:
        _moedas += _recompensaMissao3 - 50
        _missao = 3
    elif _ataque >= 20 and _defesa >= 30:
        _moedas += _recompensaMissao4
        _missao = 4
    elif _nivelPersonagem >= 5 and _defesa >= 50:
        _moedas += _recompensaMissao6
        _missao = 6
    elif _ataque >= 30 and _defesa >= 10:
        _moedas += _recompensaMissao1
        _missao = 1
    elif _moedas >= 20:
        _moedas += (_recompensaMissao4 -20)
        _missao = 4
    elif _moedas >= 30 and _defesa >= 30:
        _moedas += (_recompensaMissao2 - 30)
        _missao = 2
    else:
        _missao = 0

elif _nivelPersonagem >= 0 and _nivelPersonagem < 3: # missões 1 e 2
    if _ataque >= 30 and _defesa >= 10:
        _moedas += _recompensaMissao1
        _missao = 1
    elif _moedas >= 30 and _defesa >= 30:
        _moedas += (_recompensaMissao2 - 30)
        _missao = 2
else:
    _missao = 0

# Impressão da missão escolhida
print('missão escolhida:', _missao)
print('moedas de ouro:', _moedas)
