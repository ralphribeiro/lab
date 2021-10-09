from dataclasses import dataclass, field
from functools import lru_cache
from uuid import uuid5, NAMESPACE_DNS

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource
import numpy as np
from scipy.interpolate import griddata


@dataclass
class Ponto:
    carga: str
    número: int = field(init=False)
    x: float = field(init=False)
    y: float = field(init=False)
    z: float = field(init=False)
    referência: str = field(init=False)

    def __post_init__(self):
        sanitizado = self.carga.rstrip().split(',')
        self.número = sanitizado.pop(0)
        self.x = float(sanitizado.pop(0))
        self.y = float(sanitizado.pop(0))
        self.z = float(sanitizado.pop(0))
        self.referência = sanitizado.pop(0)


def carrega_pontos(path_):
    with open(path_, 'r') as arquivo:
        linhas = arquivo.readlines()
        ponto_zero = Ponto(linhas[0])
        pontos = []
        for raw in linhas:
            ponto = Ponto(raw)
            ponto.x -= ponto_zero.x
            ponto.y -= ponto_zero.y
            ponto.z -= ponto_zero.z
            pontos.append(ponto)
    return pontos


@lru_cache
def gera_cor(valor):
    return f'#{uuid5(NAMESPACE_DNS, valor).hex[:6]}'


def plota_2d(pontos, curvas=False):
    plt.style.use('_classic_test_patch')
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.grid(True)

    for ponto in pontos:
        ax1.scatter(
            ponto.x, ponto.y, s=4, marker='o', c=gera_cor(ponto.referência)
        )

    ax1.legend()
    plt.savefig('pontos-2D')

    if curvas:
        fig = plt.figure()
        ax2 = fig.add_subplot(111)

        x, y, z = [], [], []
        for p in pontos:
            x.append(p.x)
            y.append(p.y)
            z.append(p.z)

        xi = np.linspace(min(x), max(x))
        yi = np.linspace(min(y), max(y))
        X, Y = np.meshgrid(xi, yi)
        Z = griddata((x, y), z, (xi[None, :], yi[:, None]),
                     method='linear',  rescale=True
                     )
        cs = ax2.contour(X, Y, Z, 20, cmap=plt.cm.bone)
        ax2.clabel(cs, fontsize=8, inline=1)
        plt.savefig('curvas.png')

        fig = plt.figure()
        ax3 = fig.add_subplot(111)
        cs = ax3.contourf(X, Y, Z, 20, cmap=plt.cm.CMRmap, alpha=0.3)
        ax3.clabel(cs, fontsize=8, inline=1)
        plt.savefig('curvas_cor.png')


def set_aspect_equal_3d(ax):
    """Fix equal aspect bug for 3D plots."""

    xlim = ax.get_xlim3d()
    ylim = ax.get_ylim3d()
    zlim = ax.get_zlim3d()

    xmean = np.mean(xlim)
    ymean = np.mean(ylim)
    zmean = np.mean(zlim)

    plot_radius = max([abs(lim - mean_)
                       for lims, mean_ in ((xlim, xmean),
                                           (ylim, ymean),
                                           (zlim, zmean))
                       for lim in lims])

    ax.set_xlim3d([xmean - plot_radius, xmean + plot_radius])
    ax.set_ylim3d([ymean - plot_radius, ymean + plot_radius])
    ax.set_zlim3d([zmean - plot_radius, zmean + plot_radius])


def plota_3d(pontos, curvas=False):
    x, y, z = [], [], []
    for p in pontos:
        x.append(p.x)
        y.append(p.y)
        z.append(p.z)

    xi = np.linspace(min(x), max(x))
    yi = np.linspace(min(y), max(y))
    X, Y = np.meshgrid(xi, yi)

    Z = griddata((x, y), z, (xi[None, :], yi[:, None]),
                 method='nearest', rescale=True
                 )

    # Set up plot
    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

    ls = LightSource(270, 45)
    # To use a custom hillshading mode, override the built-in shading and pass
    # in the rgb colors of the shaded surface calculated from "shade".
    rgb = ls.shade(Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=rgb,
                           linewidth=0, antialiased=False, shade=False)
    set_aspect_equal_3d(ax)
    plt.show()


def main():
    pontos = carrega_pontos('pontos.txt')
    plota_2d(pontos, True)


main()
