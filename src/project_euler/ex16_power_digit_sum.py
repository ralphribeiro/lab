from itertools import accumulate


def power_dig_sum(e: int) -> int:
    return max(accumulate(int(a) for a in str(2**e)))


assert power_dig_sum(15) == 26


r = power_dig_sum(1000)
print(r)
