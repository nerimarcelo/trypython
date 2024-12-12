# Aula 5: Funções em Python para Programadores de Shellscript

## Objetivos da Aula
- Compreender a definição e uso de funções em Python
- Comparar funções de Python com shellscript
- Explorar diferentes tipos de passagem de parâmetros
- Entender escopo de variáveis
- Introduzir funções lambda

## Fundamentos de Funções: Comparação Shellscript vs Python

### Shellscript: Definição de Funções
```bash
# Função no shellscript
function saudacao() {
    echo "Olá, $1!"
}

# Chamada de função
saudacao "Mundo"
```

### Python: Definição de Funções
```python
# Função equivalente em Python
def saudacao(nome):
    print(f"Olá, {nome}!")

# Chamada de função
saudacao("Mundo")
```

## Definição Básica de Funções

### Funções Simples
```python
# Função sem parâmetros
def saudacao_padrao():
    print("Olá, Mundo!")

# Função com parâmetros
def soma(a, b):
    return a + b

# Chamadas
saudacao_padrao()
resultado = soma(5, 3)
print(resultado)  # Imprime 8
```

## Parâmetros e Argumentos

### Parâmetros Padrão
```python
# Parâmetros com valores padrão
def saudacao(nome="Mundo", saudacao="Olá"):
    print(f"{saudacao}, {nome}!")

# Diferentes formas de chamada
saudacao()  # Usa valores padrão
saudacao("João")  # Apenas nome
saudacao("Maria", "Bom dia")  # Ambos os parâmetros
```

### Argumentos Nomeados
```python
# Passagem de argumentos por nome
def criar_usuario(nome, idade, cidade="Não informada"):
    return {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

# Flexibilidade na ordem
usuario = criar_usuario(idade=30, nome="João")
```

### Número Variável de Argumentos
```python
# Argumentos variádicos
def soma_todos(*numeros):
    return sum(numeros)

print(soma_todos(1, 2, 3, 4, 5))  # Soma 15

# Argumentos nomeados variádicos
def imprimir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprimir_info(nome="João", idade=30, profissao="Programador")
```

## Escopo de Variáveis

### Variáveis Locais e Globais
```python
# Variável global
total = 0

def calcular(valor):
    # Escopo local
    resultado = valor * 2
    
    # Modificar variável global
    global total
    total += resultado
    
    return resultado

print(calcular(5))  # Retorna 10
print(total)        # Acumula 10
```

### Funções Aninhadas e Escopo
```python
def funcao_externa(x):
    def funcao_interna(y):
        return x + y
    
    return funcao_interna

soma_cinco = funcao_externa(5)
print(soma_cinco(3))  # Retorna 8
```

## Funções Lambda (Funções Anônimas)
```python
# Função lambda simples
dobrar = lambda x: x * 2
print(dobrar(5))  # Retorna 10

# Uso com funções de ordem superior
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]
```

## Retorno de Múltiplos Valores
```python
def calcular_estatisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minimo, maximo, media = calcular_estatisticas([1, 2, 3, 4, 5])
```

## Exercícios Propostos

### Exercício 1: Calculadora Modular
Crie uma calculadora com funções para:
- Soma
- Subtração
- Multiplicação
- Divisão
- Potenciação
Adicione tratamento de erros e validações

### Exercício 2: Gerenciador de Contatos
Desenvolva um sistema de gerenciamento de contatos que:
- Permita adicionar contatos
- Buscar contatos
- Remover contatos
- Usar funções para cada operação
- Validar entradas

### Exercício 3: Processador de Texto
Crie funções para:
- Contar palavras em um texto
- Converter texto para maiúsculas/minúsculas
- Remover espaços extras
- Verificar palíndromos
- Usar funções lambda quando possível

## Diferenças para Shellscript
1. Declaração mais clara e estruturada
2. Escopo de variáveis mais definido
3. Suporte a funções anônimas (lambda)
4. Passagem de argumentos mais flexível
5. Retorno múltiplo de valores

## Dicas Importantes
- Use funções para modularizar código
- Prefira funções puras quando possível
- Minimize o uso de variáveis globais
- Documente suas funções
- Use type hints para clareza

## Próxima Aula
Na próxima aula, abordaremos:
- Programação orientada a objetos
- Classes e objetos
- Herança
- Métodos e atributos

Alguma dúvida sobre funções em Python?
