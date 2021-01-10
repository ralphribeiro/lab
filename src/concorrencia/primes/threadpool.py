from concurrent import futures
import time
import os

from primes import is_prime, NUMBERS


def prime_test(n):
    t0 = time.perf_counter()
    return (is_prime(n), time.perf_counter() - t0)


def main(workers):
    print(f'Workers: {workers} threads')

    t0 = time.perf_counter()
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_map = {executor.submit(prime_test, n): n
                      for n in NUMBERS}
        for future in futures.as_completed(future_map):
            n = future_map[future]
            res, dt = future.result()
            msg = 'is' if res else 'is not'
            print(f'({dt:0.3f}s) {n:18d} {msg} prime')
    dt = time.perf_counter() - t0
    print(f'Workers: {workers} threads\nTotal time: {dt:0.3f}s')


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        num_workers = int(sys.argv[1])
    else:
        num_workers = os.cpu_count()

    main(num_workers)
