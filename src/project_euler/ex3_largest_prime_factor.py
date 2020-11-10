"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
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
def calc_factor(n):
    primes = (p for p in range(2, n) if not
              [t for t in range(2, p) if not p % t])
    p = next(primes)
    while n > p:
        if n % p == 0:
            n //= p
        else:
            p = next(primes)
    return print(n)


calc_factor(13195)
calc_factor(600851475143)
