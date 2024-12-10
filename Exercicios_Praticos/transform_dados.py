lista_inicial = [1,2,3,4,4,4,4,4,5,5,5,5,6,7,8,8,10.191,1290,150,178]

nova_lista = pares = [x for x in lista_inicial if x % 2 == 0]

print("Apenas pares")
print(nova_lista)
print("lista ordenada de forma decrescente")
nova_lista.reverse()
print(nova_lista)