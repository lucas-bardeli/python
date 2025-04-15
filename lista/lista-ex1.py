
numeros = [1, 2, 3]

print(type(numeros))

numeros.append(4)
numeros.append(5)
numeros.append(600)
print(len(numeros))

numeros[3] = 100
numeros.insert(0, 200)

print(numeros[6])
print(numeros[-1])
print(numeros[-2])
print(7 in numeros)
print(numeros)