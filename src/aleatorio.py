from itertools import chain, accumulate
from operator import add


def nested_sum(lista: list):
    return max(list(accumulate(chain.from_iterable(lista), add)))

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))


def cumsum(lista: list):
    return list(accumulate(lista))

t = [1, 2, 3]
print(cumsum(t))


def middle(lista: list):
    return lista[1:-1]

t = [1, 2, 3, 4]
print(middle(t))


def middle(lista: list):
    lista.pop(0)
    lista.pop(-1)

t = [1, 2, 3, 4]
middle(t)
print(t)


def is_sorted(lista: list):
    return lista == sorted(lista)

v = [1, 2, 2]
print(is_sorted(v))
v = ['b', 'a']
print(is_sorted(v))


# https://pense-python.caravela.club/10-listas/15-exercicios.html