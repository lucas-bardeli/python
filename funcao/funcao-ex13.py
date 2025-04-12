# Desenvolva um algoritmo em Python para determinar 
# se o número é par ou impar.
# O algoritmo deve:
# - Pedir ao usuáruio um número
# - Por meio de uma função que recebe o número como parâmetro,
#   determine se o parâmetro é par ou impar. 
# - A função deve retornar True para par e False para ímpar.
# - Mostrar ao usuário o resultado.


def numero_par_ou_impar(numero):
    return numero % 2 == 0


numero = int(input("\nInforme um número: "))

if numero_par_ou_impar(numero):
    print()
    print(f"O número {numero} é par.")
    print()
else:
    print()
    print(f"O número {numero} é ímpar.")
    print()