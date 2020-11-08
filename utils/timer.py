from time import perf_counter_ns


def timer(func):
    def inner(*args):
        inicio = perf_counter_ns()
        r = func(*args)
        fim = perf_counter_ns()
        print(f'{func.__name__}(): {(fim-inicio)/10**6}ms')
        return r
    return inner
