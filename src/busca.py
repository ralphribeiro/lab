# BUSCA-BINÁRIA(V[], início, fim, e)
#     i recebe o índice do meio entre início e fim
#     se (v[i] = e) entao
#         devolva o índice i   # elemento e encontrado
#     fimse
#     se (inicio = fim) entao
#         não encontrou o elemento procurado
#     senão
#        se (V[i] vem antes de e) então
#           faça a BUSCA-BINÁRIA(V, i+1, fim, e)
#        senão
#           faça a BUSCA-BINÁRIA(V, inicio, i-1, e)
#        fimse
#     fimse

from time import perf_counter_ns


def cria_lista_ordenada(range_: int) -> list:
    return range(range_)

def busca_linear(lista: list, n: int):
    for x in lista:
        if x == n:
            return x


def busca_binaria_sem_recursao(lista: list, item: int):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == item:
            return item
        else:
            if item < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1


def busca_binaria_recursao(lista: list, item: int):
    if len(lista) > 0:
        meio = len(lista)//2
        if lista[meio] == item:
            return item
        else:
            if item < lista[meio]:
                return busca_binaria_recursao(lista[:meio], item)
            else:
                return busca_binaria_recursao(lista[meio+1:], item)
