frutas = ["maca", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5, 6]
lista_mista = [1, 2, 3, "banana", 4, 5, 6, "laranja"]
lista_vazia = []
# Acessando elementos
print("Primeiro elemento")
print(frutas[0])
print("---------")
print("Ultimo elemento")
print(numeros[-1])
print("---------")
print("Lista fatiada - slice")
print(frutas[1:4])
print("---------")
print("Lista completa")
print(frutas)
# Modificando listas
print("Adicionando ao final da lista")
frutas.append("uva")
print(frutas)
print("Adicionando numa posicao especifica")
frutas.insert(1, "manga")
print(frutas)
posicao = int(input("Insira uma posicao "))
fruta_nova = input("Insira uma nova fruta ")
print(frutas)
frutas.insert(posicao, fruta_nova)
print(frutas)
print("Removendo elementos direto - acha o primeiro e remove")
print(frutas)
frutas.remove("uva")
print(frutas)
print("Removendo elementos por indice")
del frutas[1]
print("Removendo a segunda fruta")
print(frutas)
print("Removendo e retorna o ultimo elemento")
ultimo = frutas.pop()
print(frutas)
print(ultimo)

for fruta in frutas:
    print(fruta)

print("--------------------------------")
# Cria 2 indices de iteracao e roda dentro da lista
for indice, fruta in enumerate(frutas):
    print(f"Indice {indice}: {fruta}")
