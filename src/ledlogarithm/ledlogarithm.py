from math import log
from matplotlib import pyplot as plt


def monta(intervalo, base, passo):
    ll = [log(x, base) for x in range(intervalo[0], intervalo[1], passo)]
    plt.plot(ll, label=base)


for b in range(2, 20):
    monta((1, 255), b, 1)


plt.legend()
plt.show()
