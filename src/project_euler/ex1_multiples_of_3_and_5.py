"""
Multiples of 3 and 5.

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from datetime import datetime


def time_delta(func):
    def inner(*args):
        t_init = datetime.now()
        func(*args)
        t_final = datetime.now() - t_init
        print(f'{t_final.seconds}s | {t_final.microseconds}us')
        return time_delta
    return inner


@time_delta
def calc_all_multiple(m):
    num_de_0_10 = [n for n in range(3, m) if n % 3 == 0 or n % 5 == 0]
    soma = sum(n for n in num_de_0_10)
    print(num_de_0_10, soma)


calc_all_multiple(10)
calc_all_multiple(1000)
