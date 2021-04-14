from dataclasses import FrozenInstanceError
from decimal import Decimal, DivisionByZero
from random import choice, randint, random, Random

from pytest import raises

from .tmp import Moeda, ExceçãoMoedaDiferente

ALFAB = [chr(n) for n in range(65, 91)]


def nome_aleatorio():
    return ''.join(choice(ALFAB) for _ in range(3))


def quantidade_aleatoria():
    return Decimal(randint(0, 10**6) + random())


def test_cria_um_valor_moeda():
    nome, quantidade = nome_aleatorio(), quantidade_aleatoria()
    moeda = Moeda(nome, quantidade)

    assert moeda.nome == nome
    assert moeda.quantidade == quantidade


def test_imutabilidade_da_moeda():
    moeda = Moeda(nome_aleatorio(), quantidade_aleatoria())
    with raises(FrozenInstanceError):
        print(moeda.nome)
        moeda.nome = 'teste'
        print(moeda.nome)



def test_sucesso_soma_duas_moedas_com_o_mesmo_nome():
    nome1, quantidade1 = nome_aleatorio(), quantidade_aleatoria()
    quantidade2 = quantidade_aleatoria()
    m1 = Moeda(nome1, quantidade1)
    m2 = Moeda(nome1, quantidade2)
    esperado = Moeda(nome1, (quantidade1 + quantidade2))
    assert m1 + m2 == esperado


def test_falha_soma_duas_moedas_com_nomes_diferentes():
    nome1, quantidade1 = 'ABC', quantidade_aleatoria()
    nome2, quantidade2 = 'DEF', quantidade_aleatoria()
    m1 = Moeda(nome1, quantidade1)
    m2 = Moeda(nome2, quantidade2)
    with raises(ExceçãoMoedaDiferente):
        m1 + m2


def test_sucesso_subtração_duas_moedas_com_o_mesmo_nome():
    nome1, quantidade1 = nome_aleatorio(), quantidade_aleatoria()
    quantidade2 = quantidade_aleatoria()
    m1 = Moeda(nome1, quantidade1)
    m2 = Moeda(nome1, quantidade2)
    esperado = Moeda(nome1, (quantidade1 - quantidade2))
    assert m1 - m2 == esperado


def test_falha_subtração_duas_moedas_com_nomes_diferentes():
    nome1, quantidade1 = 'ABC', quantidade_aleatoria()
    nome2, quantidade2 = 'DEF', quantidade_aleatoria()
    m1 = Moeda(nome1, quantidade1)
    m2 = Moeda(nome2, quantidade2)
    with raises(ExceçãoMoedaDiferente):
        m1 - m2


def test_sucesso_multiplicação_duas_moedas_com_o_mesmo_nome():
    nome1, quantidade1 = nome_aleatorio(), quantidade_aleatoria()
    quantidade2 = quantidade_aleatoria()
    m1 = Moeda(nome1, quantidade1)
    m2 = Moeda(nome1, quantidade2)
    esperado = Moeda(nome1, (quantidade1 * quantidade2))
    assert m1 * m2 == esperado


def test_falha_multiplicação_duas_moedas_com_nomes_diferentes():
    nome1, quantidade1 = 'ABC', quantidade_aleatoria()
    nome2, quantidade2 = 'DEF', quantidade_aleatoria()
    m1 = Moeda(nome1, quantidade1)
    m2 = Moeda(nome2, quantidade2)
    with raises(ExceçãoMoedaDiferente):
        m1 * m2


def test_sucesso_divisão_duas_moedas_com_o_mesmo_nome():
    nome1, quantidade1 = nome_aleatorio(), quantidade_aleatoria()
    quantidade2 = quantidade_aleatoria()
    m1 = Moeda(nome1, quantidade1)
    m2 = Moeda(nome1, quantidade2)
    esperado = Moeda(nome1, (quantidade1 / quantidade2))
    assert m1 / m2 == esperado


def test_falha_divisão_duas_moedas_com_nomes_diferentes():
    nome1, quantidade1 = 'ABC', quantidade_aleatoria()
    nome2, quantidade2 = 'DEF', quantidade_aleatoria()
    m1 = Moeda(nome1, quantidade1)
    m2 = Moeda(nome2, quantidade2)
    with raises(ExceçãoMoedaDiferente):
        m1 / m2


def test_moedas_erro_dividido_por_zero():
    nome1, quantidade1 = 'ABC', quantidade_aleatoria()
    m1 = Moeda(nome1, quantidade1)
    m2 = Moeda(nome1, Decimal(0.0))
    with raises(DivisionByZero):
        m1 / m2
