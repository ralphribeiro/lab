from unittest import TestCase
from ..exercices.ex12_highly_div_triangular_num import (gen_triangular_nums_on,
                                                        get_divisors_of,
                                                        get_len)


class TestEx11(TestCase):
    def test_5_firts_triangular_nums_must_be_1_3_6_10_15(self):
        chamada = 5
        esperado = [1, 3, 6, 10, 15]
        retorno = gen_triangular_nums_on()
        for i in range(chamada):
            self.assertEqual(esperado[i], next(retorno))

    def test_10_firts_triangular_nums_must_be_1_3_6_10_15_21_28_36_45_55(self):
        chamada = 10
        esperado = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        retorno = gen_triangular_nums_on()
        for i in range(chamada):
            self.assertEqual(esperado[i], next(retorno))

    def test_divisors_of_15_must_be_1_3_5_15(self):
        chamada = 15
        esperado = [1, 3, 5, 15]
        retorno = get_divisors_of(chamada)
        self.assertEqual(esperado, list(retorno))

    def test_divisors_of_28_must_be_1_2_4_7_14_28(self):
        chamada = 28
        esperado = [1, 2, 4, 7, 14, 28]
        retorno = get_divisors_of(chamada)
        self.assertEqual(esperado, list(retorno))

    def test_size_of_div_of_triangular_num_must_be_6(self):
        chamada = 5
        esperado = 5
        retorno = get_len(chamada)
        self.assertEqual(esperado, retorno)
