from itertools import chain
from unittest import TestCase
from unittest.case import skip

from src.arvore import Node


class TesteNós(TestCase):
    def test_deve_retornar_repr_o_nome_e_profundidade_padronizado_dado_nome(self):
        self.assertEqual('nó(mapa mental)', repr(Node('mapa mental')))

    def test_deve_retornar_um_iterável_de_nós_ao_adicionar_nós_filhos(self):
        nó_raiz = Node('mapa mental')
        filhos = ('Python', 'linux', 'testes')

        for f in filhos:
            nó_raiz.add_child(Node(f))

        for c in nó_raiz:
            self.assertIsInstance(c, Node)

    def test_filho_deve_ter_uma_referencia_fraca_com_o_pai(self):
        pai = Node('pai')
        filho = Node('filho')
        pai.add_child(filho)
        self.assertEqual(filho.parent, pai)
        del pai
        self.assertEqual(filho.parent, None)

    # @skip("desenvolvimento depth_first")
    def test_depth_first(self):
        pai = Node('1')

        filhos = ('2', '3')
        netos = (['4', '5', '6'], ['7', '8', '9'])
      
        nos_f = [Node(f) for f in filhos]

        for i, f in enumerate(nos_f):
            for n in netos[i]:
                f.add_child(Node(n))
            pai.add_child(f)

        esperado = [1, 2, 4, 5, 6, 3, 7, 8, 9]

        for c, e in zip(pai.depth_first(), esperado):
            self.assertEqual(f'nó({e})', repr(c))