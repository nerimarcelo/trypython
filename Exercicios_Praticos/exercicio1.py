print("--- Verifica Idade e Ingresso ---")

idade = int(input("Digite a idade: "))
idadeMeia = 65
ingresso = 40

if idade >= 18:
    print(f"Liberado, cliente tem {idade} anos")
elif idade < 18:
    print(f"Barrado, cliente tem {idade} anos e a entrada \
eh apenas para maiores de 18 anos")
if idade >= idadeMeia:
    print("Cliente tem direito a meia entrada")
    meiaEntrada = ingresso/2
    ingresso = meiaEntrada

print(f"Valor a ser pago sera de {ingresso}")