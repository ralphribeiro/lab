"""
10001st prime.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

@time_delta
def calc_prime_by_num(num):
    prime = gen_primes()
    ret = max(next(prime) for _ in range(num))
    return print(ret)


calc_prime_by_num(6)
calc_prime_by_num(10001)
