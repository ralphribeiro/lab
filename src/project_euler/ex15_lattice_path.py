from math import factorial

def lattice_paths(w: int, h: int):
    return factorial(w+h)//(factorial(w)*factorial(h))

print(lattice_paths(2, 2))
print(lattice_paths(20, 20))