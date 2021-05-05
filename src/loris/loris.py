from pprint import pprint
from time import perf_counter_ns, sleep


from matplotlib import pyplot as plt


def timer(func):
    def inner(*args):
        init = perf_counter_ns()
        func(*args)
        return (perf_counter_ns()-init)/10**6
    return inner


@timer
def capitaliza(str_: str, n: int):
    for _ in range(n):
        ' '.join([n.capitalize() for n in str_.split()])


@timer
def capitaliza2(str_: str, n: int):
    for _ in range(n):
        str_.title()


with open('loris.txt', 'r') as file:
    text = file.read()


vzs = 200

data = [capitaliza(text, d) for d in range(vzs)]
data2 = [capitaliza2(text, d) for d in range(vzs)]


plt.plot(data, label='capitaliza')
plt.plot(data2, label='capitaliza2')
plt.xlabel('vezes')
plt.ylabel('ms')
plt.legend()
plt.grid(True)
plt.show()
