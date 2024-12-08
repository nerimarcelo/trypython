Converta o seguinte script shellscript para Python:

```bash
#!/bin/bash

echo "Calculadora Simples"
read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2
read -p "Escolha a operação (+, -, *, /): " operacao

case $operacao in
    "+")
        resultado=$(($num1 + $num2))
        ;;
    "-")
        resultado=$(($num1 - $num2))
        ;;
    "*")
        resultado=$(($num1 * $num2))
        ;;
    "/")
        resultado=$(($num1 / $num2))
        ;;
    *)
        echo "Operação inválida"
        exit 1
esac

echo "Resultado: $resultado"

Resultado: calculadora.py