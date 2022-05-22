from collections import Counter
from random import choice
from requests import get
from time import perf_counter_ns


def timer(func):
    def inner():
        started = perf_counter_ns()
        ret = func()
        finished = perf_counter_ns() - started
        fail = ret.status_code >= 400
        return (ret, {'time': finished, 'fail': fail})
    return inner


@timer
def me_da():
    response = get('http://192.168.1.6:80/helloWorld')
    return response


@timer
def configs():
    response = get('http://192.168.1.6:80/settings')
    return response


def main(num):
    funcs = configs, me_da
    started = perf_counter_ns()
    responses = [choice(funcs)() for _ in range(num)]
    finished = perf_counter_ns() - started

    total_time = f'tempo total: {finished/10**9:.3f}s'
    failures = [r[1]['fail'] for r in responses]
    fails = Counter(failures)

    print(f'taxa: {(finished/num)/10**9:.3f}s por requisição')
    print(f'falhas: {fails["True"]}')
    print(total_time)

