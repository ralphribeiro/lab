from dataclasses import dataclass, field
from math import sqrt
from random import randrange

from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib.animation as animation


@dataclass
class Ponto:
    x: float
    y: float
    z: float


@dataclass
class Linha:
    orig: Ponto
    dest: Ponto
    tamanho: float = field(init=False)

    def __post_init__(self):
        delta_x = self.dest.x - self.orig.x
        delta_y = self.dest.y - self.orig.y
        delta_z = self.dest.z - self.orig.z
        self.tamanho = sqrt((delta_x)**2 + (delta_y)**2 + (delta_z)**2)


A = Ponto(0, 0, 0)
B = Ponto(0, 20, 0)
C = Ponto(20, 20, 0)
D = Ponto(20, 0, 0)

pontos_fixos = A, B, C, D


style.use('fivethirtyeight')

fig = plt.figure(dpi=100)
ax = fig.gca(projection='3d')



def plota_normais(*args):
    ponto_querido = ponto_aleatorio()
    ax.clear()      
    ax.scatter(ponto_querido.x, ponto_querido.y,
               ponto_querido.z, linewidth=5, c='k')

    for ponto in pontos_fixos:
        linha = Linha(orig=ponto_querido, dest=ponto)
        ax.scatter(ponto.x, ponto.y, ponto.z, linewidth=2)
        ax.plot((ponto_querido.x, ponto.x),
                (ponto_querido.y, ponto.y),
                (ponto_querido.z, ponto.z),
                label=round(linha.tamanho, 3),
                linewidth=0.7)


    ponto_querido = Ponto(1, 15, -40)

    ax.set_xlabel('X', fontsize='xx-small')
    ax.set_ylabel('Y', fontsize='xx-small')
    ax.set_zlabel('Z', fontsize='xx-small')
    # ax.
    ax.legend(fontsize='xx-small')


def ponto_aleatorio():
    x = randrange(5, 15)
    y = randrange(5, 15)
    z = -20
    print()
    return Ponto(x, y, z)



ani = animation.FuncAnimation(plt.gcf(), plota_normais, 100)
plt.tight_layout()

plt.show()
