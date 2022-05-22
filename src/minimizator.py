from string import ascii_letters
from random import choice, randint, sample
from itertools import repeat


def make_list(size, range_):
    ret = []
    for _ in range(size):
        chars = ''
        for _ in range(randint(1, range_ + 1)):
            chars += choice(ascii_letters)
        ret.append(chars)
        del(chars)
    return ret


def make_list_sample(size, range_):
    ret = []
    for _ in range(size):
        ret.append(sample(list(ascii_letters), k=randint(1, range_ + 1)))
    return ret


def split_list(list_, divisor=1):
    length, remainder = divmod(len(list_), divisor)
    ret = []
    for n in range(divisor):
        r_param = (n + 1) * length if n + \
            1 < divisor else ((n + 1) * length) + remainder
        ret.append(list_[n * length: r_param])
    return ret


lista = make_list(13, 10)
s_l = split_list(lista, 3)

print(s_l)
