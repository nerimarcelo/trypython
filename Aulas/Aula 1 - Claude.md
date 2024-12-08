# Aula 1 - Claude

Olá! Como professor de programação, vou preparar uma série de aulas para ajudar um programador de shellscript a aprender Python. Vamos começar com uma introdução comparativa entre shellscript e Python, destacando as principais diferenças e semelhanças.

# Aula 1: Introdução ao Python para Programadores de Shellscript

## Objetivos da Aula:
- Comparar shellscript e Python
- Configurar o ambiente de desenvolvimento
- Entender os conceitos básicos de Python

## Instalação e Ambiente
Para começar, instale Python:
```bash
# No Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# No CentOS/Fedora
sudo dnf install python3 python3-pip

# Verificar instalação
python3 --version
pip3 --version
```

## Comparação Inicial: Shellscript vs Python

### 1. Declaração e Execução
- Shellscript:
```bash
#!/bin/bash
echo "Olá Mundo!"
```

- Python:
```python
# hello.py
print("Olá Mundo!")
```

### 2. Variáveis
- Shellscript:
```bash
nome="João"
idade=25
```

- Python:
```python
nome = "João"
idade = 25
```

### 3. Estruturas Condicionais
- Shellscript:
```bash
if [ $idade -ge 18 ]; then
    echo "Maior de idade"
else
    echo "Menor de idade"
fi
```

- Python:
```python
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

## Exercícios Práticos

### Exercício 1: Conversão de Script Shellscript para Python
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
```

### Solução do Exercício 1:
```python
print("Calculadora Simples")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

try:
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        print("Operação inválida")
        exit(1)
    
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
```

## Principais Diferenças
1. Python usa indentação para definir blocos de código
2. Não precisa de `then` ou `fi` como no bash
3. Usa `elif` em vez de `elif`
4. Tratamento de erros mais robusto
5. Tipagem dinâmica mais flexível

## Próxima Aula
Na próxima aula, vamos aprofundar:
- Listas e manipulação de arrays
- Funções
- Tratamento de arquivos

    Vou expandir sobre o `try-except` em Python, fazendo um paralelo com tratamento de erros no shellscript.

## Tratamento de Erros: try-except em Python

### Comparação Shellscript vs Python

#### Shellscript (tratamento limitado):
```bash
# Shellscript tem opções limitadas de tratamento de erro
if [ -f arquivo.txt ]; then
    cat arquivo.txt
else
    echo "Erro: Arquivo não encontrado"
    exit 1
fi
```

#### Python (tratamento robusto):
```python
try:
    # Bloco de código que pode gerar exceção
    with open('arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

except FileNotFoundError:
    # Tratamento específico para arquivo não encontrado
    print("Erro: Arquivo não encontrado")

except PermissionError:
    # Tratamento de erro de permissão
    print("Erro: Sem permissão para ler o arquivo")

except Exception as erro:
    # Tratamento genérico para qualquer outro erro
    print(f"Erro inesperado: {erro}")

else:
    # Bloco executado se nenhum erro ocorrer
    print("Arquivo lido com sucesso")

finally:
    # Bloco sempre executado, com ou sem erro
    print("Operação de leitura concluída")
```

### Tipos Comuns de Exceções
- `FileNotFoundError`: Arquivo não encontrado
- `TypeError`: Operação com tipos incompatíveis
- `ValueError`: Valor inadequado
- `ZeroDivisionError`: Divisão por zero
- `IndexError`: Índice fora do intervalo
- `KeyError`: Chave não encontrada em dicionário

### Exemplos Práticos

#### Exemplo 1: Divisão Segura
```python
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero")
        return None

# Uso
print(dividir(10, 2))   # Funciona normalmente
print(dividir(10, 0))   # Trata erro de divisão por zero
```

#### Exemplo 2: Conversão de Tipos
```python
def converter_idade(idade_str):
    try:
        idade = int(idade_str)
        return idade
    except ValueError:
        print(f"Erro: '{idade_str}' não é um número válido")
        return None

# Uso
print(converter_idade("25"))     # Converte corretamente
print(converter_idade("vinte"))  # Trata erro de conversão
```

#### Exemplo 3: Múltiplas Exceções
```python
def processar_lista(lista, indice):
    try:
        valor = lista[indice]
        return valor * 2
    except IndexError:
        print(f"Erro: Índice {indice} não existe na lista")
    except TypeError:
        print("Erro: Não é possível multiplicar este valor")

# Uso
numeros = [1, 2, 3]
print(processar_lista(numeros, 1))   # Funciona
print(processar_lista(numeros, 5))   # Índice inválido
print(processar_lista(numeros, '2')) # Tipo inválido
```

### Criando Exceções Personalizadas
```python
class IdadeInvalidaError(Exception):
    """Exceção para idades inválidas"""
    pass

def validar_idade(idade):
    try:
        if idade < 0 or idade > 120:
            raise IdadeInvalidaError("Idade fora do intervalo aceitável")
        return idade
    except IdadeInvalidaError as e:
        print(f"Erro de validação: {e}")
        return None

# Uso
print(validar_idade(30))   # Válido
print(validar_idade(-5))   # Lança exceção personalizada
```

### Exercício Prático
Crie um script que:
1. Peça ao usuário para digitar dois números
2. Ofereça opções de operação (soma, subtração, divisão)
3. Use `try-except` para tratar:
   - Entrada não numérica
   - Divisão por zero
   - Operação inválida

### Diferenças para Shellscript
1. Tratamento de erros mais granular
2. Possibilidade de criar exceções personalizadas
3. Mecanismo de `try-except-else-finally`
4. Menos verboso que estruturas de erro no bash

## Dicas Finais
- Use exceções para situações excepcionais
- Seja específico no tratamento de erros
- Evite usar `try-except` para controle de fluxo normal
- Log erros quando possível

Quer que eu desenvolva a solução do exercício prático ou tem alguma dúvida sobre tratamento de exceções?