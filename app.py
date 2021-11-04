n: int = 1000  # sequence size
array: list = [None] * n  # storage list
seed: float = 1  # generator's seed
m: int = 2147483647  # prime number
a: int = 25717  # parameter alpha -> improve the random

for i in range(n):
    aux = (a * seed) % m
    array[i] = seed / (m - 1)
    seed = aux

print(array)


