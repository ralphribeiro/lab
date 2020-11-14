from itertools import chain, accumulate, permutations
from collections import Counter
from operator import add

# 10.1


def nested_sum(lista: list):
    return max(list(accumulate(chain.from_iterable(lista), add)))


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))

# 10.2


def cumsum(lista: list):
    return list(accumulate(lista))


t = [1, 2, 3]
print(cumsum(t))

# 10.3


def middle(lista: list):
    return lista[1:-1]


t = [1, 2, 3, 4]
print(middle(t))

# 10.4


def middle(lista: list):
    lista.pop(0)
    lista.pop(-1)


t = [1, 2, 3, 4]
middle(t)
print(t)

# 10.5


def is_sorted(lista: list):
    return lista == sorted(lista)


v = [1, 2, 2]
print(is_sorted(v))
v = ['b', 'a']
print(is_sorted(v))

# 10.6


def is_anagram(s1: str, s2: str):
    return tuple([c for c in s2]) in list(permutations(s1))


s1 = 'ator'
s2 = 'rota'
print(is_anagram(s1, s2))

# 10.7


def has_duplicates(lista: list):
    c = Counter(lista)
    for _, e in c.most_common():
        if e > 1:
            return True
    return False


lst = ['p', 'a', 'p', 'i', 'b', 'a', 'q', 'u', 'i', 'g', 'r', 'a', 'f', 'o']
print(has_duplicates(lst), lst)
lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(has_duplicates(lst), lst)

# 10.8

def birthday_paradox(n):
    p = (1.0/365)**n
    for i in range((366-n), 366):
        p *= i
    return f'{(1 - p) * 100:.1f}%'


print(birthday_paradox(23))


# https://pense-python.caravela.club/10-listas/15-exercicios.html
