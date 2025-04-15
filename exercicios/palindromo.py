# Lista de Palíndromos:
# Dada uma lista de palavras, você deve determinar quantas dessas palavras são palíndromos.
# Um palíndromo é uma palavra que pode ser lida da mesma forma de trás para frente.

# Exemplo:
# Entrada: ["osso", "python", "esse", "código"]
# Saída: 2

palavras = ["osso", "python", "esse", "código", "ana", "arara", "subinoonibus", "gato"]
total = 0
 
print()
for palavra in palavras:
    if (list(palavra) == list(reversed(palavra))):
        print(f"A palavra {palavra} é um palíndromo!")
        total = total + 1
    else:
        print(f"A palavra {palavra} não é um palíndromo!")

print()
print(f"O total de palíndromos é: {total}")
print()