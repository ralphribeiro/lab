from math import sqrt
from random import randint

from teste_poll import poll


def is_prime(n):
    sqrt_number = sqrt(n)
    for i in range(2, int(sqrt_number) + 1):
        if (n / i).is_integer():
            return False
    return True


def my_callback(exc, **kwargs):
    print('meu callback ', repr(exc), kwargs)


@poll(4, 1, exc=AssertionError, raise_=False, callback=my_callback, callback_args={})
def make_assert_error():
    if not is_prime(randint(0, 1000)):
        assert False
    print('acabei')

make_assert_error()