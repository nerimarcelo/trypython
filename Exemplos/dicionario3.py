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

# print("Acessando salario da Maria")
# print(empresa["funcionarios"]["maria"]["salario"])
# Resultado: 7000

# print("Agora o salario do Jao")
# print(empresa["funcionarios"]["joao"]["salario"])

# print("Acessando cargo do Joao")
# print(empresa["funcionarios"]["joao"]["cargo"])
# Resultado: Desenvolvedor

# print("Joao eh um funcionario?")
# print("joao" in empresa["funcionarios"])
# Resultado: True
