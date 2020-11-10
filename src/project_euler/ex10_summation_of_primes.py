"""
Summation of primes.


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from functools import wraps
from time import perf_counter_ns


def dec(fmt):
    ret_format = {'s': (10**9), 'ms': (10**6),
                  'us': (10**3), 'ns': 1}

    def delta_time(func):
        @wraps(func)
        def inner(*args):
            t_init = perf_counter_ns()
            func(*args)
            t_final = perf_counter_ns() - t_init
            print(f'{t_final/ret_format[fmt]:.2f} {fmt}')
            return None
        return inner
    return delta_time


def gen_primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


@dec('s')
def sum_primes_calc(n):
    primes = gen_primes()
    _sum = 0
    for _ in range(n):
        _sum += next(primes)
    return print(_sum)


sum_primes_calc(4)
sum_primes_calc(2000000)
