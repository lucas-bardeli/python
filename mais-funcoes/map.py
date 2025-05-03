
def mais_um_e_meio(nota):
    return nota + 1.5 


notas = [6.4, 7.2, 5.8, 8.4]

notas_finais = list(map(mais_um_e_meio, notas))

print(notas_finais) 


# outras maneiras:

# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5