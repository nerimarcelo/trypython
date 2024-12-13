usuario = {"nome": "João", "idade": 30}
contato = dict(telefone="123 456 789", email="nerimarcelo@local")

print(contato["email"])

preferencias = {}
preferencias["tema"] = "dark"
preferencias["linguagem"] = "Python"

print(preferencias)
print(preferencias["linguagem"])
print(usuario["idade"])
idade = usuario.get("idade", 300)
print(usuario["idade"])
usuario["profissao"] = "professor"
print(usuario)

print(usuario["idade"])
print("---")
# Iteração tradicional
for chave in usuario:
    print(f"{chave}: {usuario[chave]}")
print("---")
# Iteração elegante com .items()
for chave, valor in usuario.items():
    print(f"Chave: {chave}, Valor: {valor}")
print("---")
# Representando estruturas complexas
empresa = {
    "nome": "Tech Solutions",
    "funcionarios": {
        "joao": {
            "cargo": "Desenvolvedor",
            "salario": 5000,
            "projetos": ["Web", "Mobile"],
        },
        "maria": {
            "cargo": "Gerente",
            "salario": 7000,
            "projetos": ["Estratégia", "RH"],
        },
    },
}

pelego = empresa.get("funcionarios", 0)
print(pelego)
cargoPelego = pelego.get("joao", 0)
print(cargoPelego)

print(empresa["funcionarios"]["joao"]["projetos"][0])
