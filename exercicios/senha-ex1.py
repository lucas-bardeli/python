
senha1 = senha2 = ""

senha1 = input("\nCrie sua senha: ")

while (senha2 != senha1):
    senha2 = input("\nDigite sua senha: ")
    
    if (senha2 != senha1):
        print("\nSenha incorreta! Digite novamente.")
    else:
        print("\nSenha correta, você pode entrar!")
        print()