while True:

    senha = input("Digite uma senha: ")
    tamanho_minimo = 10
    caracterEspecial = "!@#$%^&*().?"

    # Verifica o tamanho da senha
    if len(senha) < tamanho_minimo:
        print(f"Tamanho minimo eh de {tamanho_minimo} caracteres")
        print("Try AGAIN")
    else:
        # Senha tem caracter especial
        tem_especial = False
        tem_maiusculo = False
        for caracter in senha:
            if caracter in caracterEspecial:
                tem_especial = True
            if caracter.isupper():
                tem_maiusculo = True
        # Aninhados ao else
        if not tem_especial:
            print("Senha nao tem char especial")
        if not tem_maiusculo:
            print("Senha nao tem letra grande")

        if tem_especial and tem_maiusculo:
            print("Senha atende aos requisitos")
            break
        else:
            print("Try AGAIN")
