import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import random
import numpy as np


def open_(path_='PTS-0000.csv'):
    df = pd.read_csv('PTS-0000.csv')
    # nan_df = df[df.isna().any(axis=1)]
    df.dropna(inplace=True)
    df.sort_values(by='nome', ascending=True, inplace=True)
    df['azimute'] = pd.to_numeric(df['azimute'] - 1500)
    df['angulo'] = pd.to_numeric(df['angulo'] - 500)
    df['distancia'] = pd.to_numeric(df['distancia'])
    return df


def set_aspect_equal_3d(ax):
    """Fix equal aspect bug for 3D plots."""

    xlim = ax.get_xlim3d()
    ylim = ax.get_ylim3d()
    zlim = ax.get_zlim3d()

    from numpy import mean
    xmean = mean(xlim)
    ymean = mean(ylim)
    zmean = mean(zlim)

    plot_radius = max([abs(lim - mean_)
                       for lims, mean_ in ((xlim, xmean),
                                           (ylim, ymean),
                                           (zlim, zmean))
                       for lim in lims])

    ax.set_xlim3d([xmean - plot_radius, xmean + plot_radius])
    ax.set_ylim3d([ymean - plot_radius, ymean + plot_radius])
    ax.set_zlim3d([zmean - plot_radius, zmean + plot_radius])


def get_plot(df: pd.DataFrame):
    plt.style.use('_classic_test_patch')

    # print(plt.style.available)

    fig = plt.figure(figsize=(15, 15), dpi=100)
    ax = fig.add_subplot(projection='3d')
    fig2 = plt.figure()
    ax1 = fig2.add_subplot(111)
    ax1.grid(True)

    mapa_cor = plt.cm.autumn

    for nome in df['nome'].unique():

        nome_df = df.copy()[df['nome'] == nome]
        nome_df.set_index('ponto', inplace=True)
        nome_df.sort_index(inplace=True)

        x = np.array(nome_df['azimute'].values.tolist())
        y = np.array(nome_df['angulo'].values.tolist())
        z = np.array(nome_df['distancia'].values.tolist())

        # x, y = np.meshgrid(x, y)

        ax.scatter(x, y, z, label=nome, s=10,  marker='o')
        ax1.scatter(x, y, s=8,  marker='o')

    xx = np.array(df['azimute'].values.tolist())
    yy = np.array(df['angulo'].values.tolist())
    zz = np.array(df['distancia'].values.tolist())

    xi = np.linspace(min(xx), max(xx))
    yi = np.linspace(min(yy), max(yy))
    X, Y = np.meshgrid(xi, yi)
    Z = griddata((xx, yy), zz, (xi[None, :], yi[:, None]),
                 method='nearest', rescale=True)
    ZZ = griddata((xx, yy), zz, (xi[None, :],
                                 yi[:, None]), method='linear', rescale=True)

    ax.contourf(X, Y, Z, 300, cmap=plt.cm.bone,
                corner_mask=True, alpha=0.2, origin=None)

    set_aspect_equal_3d(ax)

    CS = ax1.contour(X, Y, ZZ, 20, cmap=plt.cm.bone)
    ax1.clabel(CS, fontsize=8, inline=1)

    ax.grid(True)
    ax.legend()
    plt.show()


df = open_()
get_plot(df)