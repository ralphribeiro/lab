from unittest import TestCase

from src.ordena import cria_lista_aleatoria, ordena

class TestOrdena(TestCase):
    def test_deve_retornar_lista_aleatoria_com_tamanho_dado_valor(self):
        tamanho = 10**7
        self.assertEqual(tamanho, len(cria_lista_aleatoria(tamanho)))

    def test_deve_retornar_lista_ordenada_dada_lista(self):
        lista = cria_lista_aleatoria(10**6)
        retorno = ordena(lista)
        