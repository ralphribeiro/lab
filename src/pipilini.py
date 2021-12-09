from functools import wraps


def pipilini(*funcs):
    wraps(*funcs)
    def inner(data, funcs=funcs):
        result = data
        for f in funcs:
            result = f(result)
        return result
    return inner


def soma(valor):
    return valor + 10


def tira(valor):
    return valor - 1


valor = 30

p = pipilini(soma, tira)

print(p(valor))
