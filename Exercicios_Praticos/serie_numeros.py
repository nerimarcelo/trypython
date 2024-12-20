# Receba uma série de números do usuário
# Permita entrada até um valor de parada
# Calcule:
# Soma total
# Média
# Maior e menor valor
# Quantidade de números pares e ímpares

serieNumerica = []
pares = 0
impares = 0
separador = (
    "---------------------------------------------------------------------------------"
)
while True:
    print(f"Insira um numero na Serie Numerica [{len(serieNumerica)}]")
    print('Pra sair, digite "0"')

    entrada = int(input(" ~~> "))

    if entrada == 0:
        print(f"\tExecutando procedimentos e magias\n{separador}")
        break
    if entrada % 2 == 0:
        pares += 1
    else:
        impares += 1
    serieNumerica.append(entrada)
    # print(serieNumerica)

# Soma
soma = 0

for i in range(len(serieNumerica)):

    soma += serieNumerica[i]

# Media
media = soma / len(serieNumerica)

# Maior e menor
serieNumerica.sort()

print(serieNumerica)
print(f"\nSoma eh \t{soma}")
print(f"Media eh\t{media}")
print(f"Maior eh\t{serieNumerica[-1]}")
print(f"Menor eh\t{serieNumerica[0]}")
print(f"Tem {pares} pares e {impares} impares\n")
