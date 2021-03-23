from dataclasses import dataclass, field
from math import sqrt
from random import randrange

from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
import numpy as np


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


A = Ponto(-5, -5, 5)
B = Ponto(-5, 5, 5)
C = Ponto(5, 5, 5)
D = Ponto(5, -5, 5)

pontos_fixos = {'A': A, 'B': B, 'C': C, 'D': D}


style.use('fivethirtyeight')

fig = plt.figure(dpi=100)
ax = fig.gca(projection='3d')


def plota_normais(*args):
    ponto_querido = args[0]
    # ponto_querido = next(ponto_querido)
    ax.clear()
    ax.scatter(
        ponto_querido.x,
        ponto_querido.y,
        ponto_querido.z,
        linewidth=5,
        c='k',
        label=f'x:{ponto_querido.x:.2f}, x:{ponto_querido.z:.2f}, z:{ponto_querido.z:.2f}'
    )

    for nome, ponto in pontos_fixos.items():
        linha = Linha(orig=ponto_querido, dest=ponto)
        ax.scatter(ponto.x, ponto.y, ponto.z, linewidth=2, label=nome)
        ax.plot((ponto_querido.x, ponto.x),
                (ponto_querido.y, ponto.y),
                (ponto_querido.z, ponto.z),
                label=round(linha.tamanho, 3),
                linewidth=0.7)

    ax.set_xlabel('X', fontsize='xx-small')
    ax.set_ylabel('Y', fontsize='xx-small')
    ax.set_zlabel('Z', fontsize='xx-small')
    # ax.
    ax.legend(fontsize='xx-small')
    ax.set_zlim3d([-5, 5])


def curva_parametrica():
    size = 100
    t = 4
    theta = np.linspace(-t * np.pi, t * np.pi, size)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    for i in range(size):
        yield Ponto(x[i], y[i], z[i])


def ponto_aleatorio():
    x = randrange(5, 15)
    y = randrange(5, 15)
    z = -20
    return Ponto(x, y, z)


ani = animation.FuncAnimation(plt.gcf(), plota_normais, curva_parametrica)
plt.tight_layout()


plt.show()
