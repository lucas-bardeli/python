# Entrada e saída de dados com arquivos.

# Escrita:

nome = input("\nDigite seu nome: ")

with open("nomes.txt", "a") as arquivo:
    arquivo.write(nome + "\n")

print()
print("Nome salvo com sucesso!")
print()

# Leitura:

with open("nomes.txt", "r") as arquivo:
    for i in arquivo:
        print(i.strip())
        
print()