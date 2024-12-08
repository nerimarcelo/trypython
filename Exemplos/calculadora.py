
# print mostra coisas na tela
print("Calculadora Simples")

# input recebe o conteudo de stdin
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

operacao = input("Escola uma operacao [+ - * /] ")
resultado=0
try:
    if operacao == "+":
        tipo = "soma"
        resultado = numero1 + numero2
    elif operacao == "-":
        tipo = "subtracao"
        resultado = numero1 - numero2
    elif operacao == "*":
        tipo = "multiplicacao"
        resultado = numero1 * numero2
    elif operacao == "/":
        tipo = "divisao"
        resultado = numero1 / numero2
    else:
        print("Operacao Invalida")
        exit (1)

# Excessao padrao do pyhton para divisao por 0
except ZeroDivisionError:
    print("Divisao por zero! Nao pode")
# Tem que estar fora da identacao do else
# f function permite que eu insira uma variavel no meio da escrita
# assim como no echo "Aqui vai uma $variavel"
print(f"Resultado da {tipo} entre {numero1} e {numero2}: {resultado}")
