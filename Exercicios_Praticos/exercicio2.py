print("--- Conversor de temperaturas ---")

print("Escolha C para converter Celsius")
print("Escolha F para converter Fahrenheit")

desejoUsuario = input("C | F ~> ")
temperatura = float(input(f"Digite a temperatura em {desejoUsuario.upper()} para converter: "))

try:
    if desejoUsuario.upper() == "C":
        fahrenheit = (temperatura * 9/5) + 32
        print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} oF")
    elif desejoUsuario.upper() == "F":
        celsius = (temperatura - 32) * 5/9
        print(f"Temperatura em Celsius: {celsius:.2f} oC")
    else:
        print("Valor invalido. Por favor, digite C ou F.")
except ZeroDivisionError:
    print("Erro de divisao por Zero")
    exit