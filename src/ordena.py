from random import randint, shuffle
from time import time

from utils.timer import timer

@timer
def cria_lista_aleatoria(tamanho: int):
    return [randint(0, tamanho-1) for _ in range(tamanho)]

@timer
def ordena(lista: list):
    lista.sort()
    return lista
