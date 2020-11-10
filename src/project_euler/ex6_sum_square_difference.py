"""
Sum square difference.

The sum of the squares of the first ten natural numbers is,
        1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
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
def calc_sun_sq_diff(r):
    v1 = sum(x**2 for x in range(r+1))
    v2 = sum(x for x in range(r+1))
    v2 = v2**2
    return print(v2 - v1)


calc_sun_sq_diff(10)
calc_sun_sq_diff(100)
