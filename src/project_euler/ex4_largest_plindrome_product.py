"""
Largest palindrome product.

    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from datetime import datetime


def time_delta(func):
    # wraps(func)
    def inner(*args):
        t_init = datetime.now()
        func(*args)
        t_final = datetime.now() - t_init
        print(f'{t_final.seconds}s | {t_final.microseconds}us')
        return time_delta
    return inner


def palindrome(n1, n2):
    prod = n1 * n2
    p = str(prod)
    l_p = len(p)
    if l_p % 2 == 0:
        start_mid = int(p[:l_p//2])
        mid_inv = int(p[:(l_p//2)-1:-1])
        if start_mid == mid_inv:
            return prod
    return None


@time_delta
def calculate(n):
    n1 = 10**(n-1)
    n2 = 10**(n)

    lista = list()
    for x in range(n1, n2):
        for y in range(n1, n2):
            if p := palindrome(x, y):
                lista.append(p)
    return print(max(lista))


calculate(2)
calculate(3)
