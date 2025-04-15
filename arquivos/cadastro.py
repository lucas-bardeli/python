
def cadastrar_usuario():
    nome = input("\nDigite o nome: ")
    idade = input("Digite a idade: ")

    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{idade}\n")

    print("\nUsuário cadastrado com sucesso!")


def listar_usuarios():
    try:
        print("\nLista de usuários:")
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                nome, idade = linha.strip().split(",")
                print(f"Nome: {nome}. Idade: {idade}")
    
    except FileNotFoundError:
        print("\nO arquivo não foi criado, nenhum usuário cadastrado ainda.")


while True:
    print("\nMenu:")
    print("1 - Cadastrar usuário;")
    print("2 - Listar usuários;")
    print("3 - Sair")
    opcao = int(input("---> "))

    match opcao:
        case 1:
            cadastrar_usuario()
    
        case 2:
            listar_usuarios()
    
        case 3:
            print("\nVocê saiu!")
            print()
            break
    
        case _:
            print("\nOpção inválida!")