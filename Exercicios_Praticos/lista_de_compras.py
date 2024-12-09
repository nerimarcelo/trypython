print("= = = = LISTA DE COMPRAS = = = =")
lista_de_compras = []

while True:
    print("Escolha uma opcao:")
    print("1 - Adicionar item\n2 - Remover item\n3 - Mostrar itens\n4 - Limpar lista\n5 - Sair")
    opcaoEscolhida = int(input("Digite a opcao ~> "))
    if opcaoEscolhida == 1:
        novoItem = input("Adicione um item a lista ")
        lista_de_compras.append(novoItem)
        print(lista_de_compras)
    elif opcaoEscolhida == 2:
        removerItem = input("Qual item vamos remover? ")
        lista_de_compras.remove(removerItem)
        print(lista_de_compras)
    elif opcaoEscolhida == 3:
        print("Item das lista")
        print(lista_de_compras)
    elif opcaoEscolhida == 4:
        print("Limpando lista...")
        lista_de_compras.clear()
    elif opcaoEscolhida == 5:
        print("Sair")
        exit(0)
    else:
        print("Opcao nao encontrada")
        exit(1)
