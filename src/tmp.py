from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal


class ExceçãoMoedaDiferente(Exception):
    ...


@dataclass(frozen=True)
class Moeda:
    """
    Objeto de valor do tipo moeda
    """
    nome: str
    quantidade: Decimal

    def __add__(self, other: Moeda):
        if not self.nome == other.nome:
            raise ExceçãoMoedaDiferente
        return Moeda(self.nome, self.quantidade + other.quantidade)

    def __sub__(self, other: Moeda):
        if not self.nome == other.nome:
            raise ExceçãoMoedaDiferente
        return Moeda(self.nome, self.quantidade - other.quantidade)

    def __mul__(self, other: Moeda):
        if not self.nome == other.nome:
            raise ExceçãoMoedaDiferente
        return Moeda(self.nome, self.quantidade * other.quantidade)

    def __truediv__(self, other: Moeda):
        if not self.nome == other.nome:
            raise ExceçãoMoedaDiferente
        return Moeda(self.nome, self.quantidade / other.quantidade)


