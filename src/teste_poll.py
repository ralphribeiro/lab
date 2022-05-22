from typing import Callable, Union
from time import sleep


def poll(attempts: int,
         time_between: Union[int, float],
         *,
         exc=Exception,
         raise_: bool = True,
         callback: Callable = None,
         **callback_args):
    """
    Espera a função decorada ser executada.

    Args:
        attempts:
            Quantidade de tentativas na execução da função.
        time_between:
            Tempo de espera entre as tentativas.
        exc:
            Excessão a ser tratada.
        callback:
            Função a ser executada em caso de falha.
        callback_args:
            Argumentos do callback.

    Returns:
        Execução da função, caso a execução falhe após as tentativas
        o callback é executado e a exceção é exaltada.
    """
    def decorator(function_):
        def wrapper(*args):
            caught = None
            for attempt in range(attempts):
                print('tentativa: ', attempt)
                try:
                    return function_(*args)
                except exc as e:
                    caught = e
                    sleep(time_between)
            if callback:
                callback(caught, **callback_args)
            if raise_:
                raise caught
        return wrapper
    return decorator
