from random import randint
from unittest import TestCase

from utils.timer import timer
from src.busca import (busca_binaria_sem_recursao, cria_lista_ordenada,
                       busca_linear, busca_binaria_recursao)


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
