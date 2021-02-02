"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

from itertools import accumulate


def power_dig_sum(e: int) -> int:
    return max(accumulate(int(a) for a in str(2**e)))


assert power_dig_sum(15) == 26


r = power_dig_sum(1000)
print(r)
