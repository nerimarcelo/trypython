print("= = = Lista de notas = = =")
print("Exercicio classico")

lista_de_notas = []
cont = 0

while cont < 4:
    nota = float(input(f"Insira a nota {cont+1}/4: "))
    lista_de_notas.append(nota)
    cont = cont+1

#print(lista_de_notas)
print()

print("Media das notas")
cont = 0
soma = 0
media = 0
while cont < 4:
    # print(lista_de_notas[cont])
    soma = lista_de_notas[cont]+soma
    # print(soma)
    cont = cont+1

media = float(soma/4)
print(f"A media foi: {media:.1f}")
print()
print("Media para passar eh 7")
print()
if media < 7.0:
    print("REPROVOU")
else:
    print("APROVADO")
print()
lista_de_notas.sort()
print(f"A maior nota foi {lista_de_notas[3]} e menor nota foi {lista_de_notas[0]}")
print()
print("As notas acima da media foram")
acima_da_media = [x for x in lista_de_notas if x > 7.0]
print(acima_da_media)