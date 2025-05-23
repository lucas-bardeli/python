# Uma escola está realizando matrículas para um curso aberto à comunidade, com limite de 20 vagas. 
# Algoritmo que:
# Lê a idade e o sexo do aluno;
# Informa que a turma está lotada, quando o número de inscritos atingir a quantidade de vagas;
# Mostra a idade média dos candidatos;
# Mostra a quantidade de mulheres inscritas;
# Mostra os candidatos (homens e mulheres) maiores de idade.

idade = soma_idades = 0
idade_media = 0.0
sexo = ""
qtd_mulheres = qtd_maiores = 0

print()
for contador in range (0, 20, 1):
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M ou F): ")
    
    if (sexo == "F"):
        qtd_mulheres += 1
    else:
        print("Sexo errado informado!")
    
    if (idade >= 18):
        qtd_maiores += 1
    
    soma_idades = soma_idades + idade

idade_media = soma_idades / 20

print()
print("A turma está lotada.")
print(f"A média de idade dos inscritos é: {idade_media}")
print(f"A quantidade de mulheres inscritas é: {qtd_mulheres}")
print(f"A quantidade de alunos maiores de idade é: {qtd_maiores}")
print()