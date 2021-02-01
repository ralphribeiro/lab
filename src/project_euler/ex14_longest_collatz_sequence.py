"""
    The following iterative sequence is defined for the set of positive
    integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from concurrent import futures
from collections import defaultdict
from sys import argv


def collatz_sequence(n: int):
    ret = [n]
    while n > 1:
        n = n//2 if n % 2 == 0 else 3*n + 1
        ret.append(n)
    return len(ret), ret


def main(*args):
    init, limit = args
    largest_len = int()
    largest_seq = list()
    for n in reversed(range(init, limit)):
        len_, list_ = collatz_sequence(n)
        if len_ > largest_len:
            largest_len, largest_seq = len_, list_
    return largest_len, largest_seq


if __name__ == "__main__":
    with futures.ProcessPoolExecutor() as executor:
        future_map = defaultdict()
        step = 10**6 // 8
        init = 5
        limit = step
        for n in range(8):
            future_map.update({executor.submit(main, init, limit): n})
            limit += step
            init += (step + 1)

        res = list()
        for future in futures.as_completed(future_map):
            n = future_map[future]
            b = future.result()
            res.append(b)

        print(max(res))

