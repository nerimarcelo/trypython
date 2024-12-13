# usuario = {
#     "nome": "Marcelo",
#     "idade": 32,
#     "cidade": "Curitiba",
#     "bairro": "Cajuru"
#
# }
#
# contato = dict(telefone="5541996453649", email="nerimmarcelo@gmail.com")
#
# print(usuario["nome"])
# print(usuario["bairro"])
# print(usuario["idade"])
# print(usuario["cidade"])
# print()
# print(contato["email"])
# print(contato["telefone"])
# print("Metodos")
# # get(chave, valor)
# usuario["nome"] = "Super Marcelo"
# cidade = usuario.get("cidade", "Campo Largo")
# idade = usuario.get("idade", "Idade não definida")
#
# print(f"O {usuario['nome']} mora em {usuario['cidade']} mas deseja morar em {cidade}")
# print(f"e tem {idade} ou {usuario["idade"]}")
#
# print("--- Utilidades ---")
# print("Retorna um booleado")
# print("nome" in usuario)
# print("")
#
# # Obter todas as chaves e valores
# # mostra chave
# print(usuario.keys())
# # mostra valor
# print(usuario.values())
# # mostra chave:valor
# print(usuario.items())
# print("------------------------------------")
# # Iterar sobre chaves
# for chave in usuario:
#     print(chave, usuario[chave])
#
# # Iterar sobre itens
# for chave, valor in usuario.items():
#     print(f"{chave}: {valor}")

print("------------------------------------")

# Dicionários dentro de dicionários
empresa = {
    "nome": "Tech Solutions",
    "funcionarios": {
        "joao": {"cargo": "Desenvolvedor", "salario": 5000},
        "maria": {"cargo": "Gerente", "salario": 7000},
    },
}

# Iteracao por chave
# for chave in empresa:
#    print(chave)

# Iteracao por valor
# for valor in empresa.values():
#    print(f"Eu sou um valor: {valor}")
#    for key in valor:
#        print(f"Eu sou uma key de valor: {key}")

# Iteracao por Itens
for chave, valor in empresa.items():
    print(f"{chave}: {valor}")
