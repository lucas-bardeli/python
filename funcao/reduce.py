
from functools import reduce


def somar(a, b):
    return a + b


notas = [6.4, 7.2, 5.8, 8.4]

total = reduce(somar, notas, 0)

print(total)


# outra maneira:
# total = 0
# for n in notas:
#     total = total + n