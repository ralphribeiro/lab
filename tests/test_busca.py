from random import randint
from time import perf_counter_ns
from unittest import TestCase

from src.busca import (busca_binaria_sem_recursao, cria_lista_ordenada,
                       busca_linear, busca_binaria_recursao)


def timer(func):
    def inner(*args):
        inicio = perf_counter_ns()
        r = func(*args)
        fim = perf_counter_ns()
        print(f'tempo execução: {(fim-inicio)/10**6}ms')
        return r
    return inner


lista = cria_lista_ordenada(10**10)
n = randint(0, len(lista)-1)
print(n)


class TestBusca(TestCase):
    def test_gerar_uma_lista_com_o_tamanho_1x10_9(self):
        tamanho = len(lista)
        self.assertEqual(tamanho, len(cria_lista_ordenada(tamanho)))

    @timer
    def test_deve_fazer_uma_busca_linear_dado_num(self):
        self.assertEqual(n, busca_linear(lista, n))

    @timer
    def test_deve_fazer_uma_busca_binaria_sem_recursao(self):
        self.assertEqual(n, busca_binaria_sem_recursao(lista, n))

    @timer
    def test_deve_fazer_uma_busca_binaria_com_recursao(self):
        self.assertEqual(n, busca_binaria_recursao(lista, n))
