# Aula 4: Laços de Repetição em Python para Programadores de Shellscript

## Objetivos da Aula
- Compreender os diferentes tipos de laços em Python
- Comparar estruturas de repetição com shellscript
- Dominar `for` e `while`
- Explorar técnicas avançadas de iteração

## Fundamentos de Laços: Comparação Shellscript vs Python

### Shellscript: Laço Tradicional
```bash
# Laço for tradicional
for i in {1..5}; do
    echo $i
done

# Laço while
contador=0
while [ $contador -lt 5 ]; do
    echo $contador
    ((contador++))
done
```

### Python: Laços Modernos
```python
# Laço for equivalente
for i in range(1, 6):
    print(i)

# Laço while similar
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

## Tipos de Laços em Python

### 1. Laço `for` com `range()`
```python
# Iteração com range()
for numero in range(5):
    print(numero)  # 0, 1, 2, 3, 4

# Especificando início, fim e passo
for numero in range(2, 10, 2):
    print(numero)  # 2, 4, 6, 8
```

### 2. Laço `for` com Listas
```python
# Iteração em listas
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# Com enumerate (índice e valor)
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")
```

### 3. Laço `while`
```python
# Laço while básico
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# While com condição complexa
while True:
    entrada = input("Digite algo (ou 'sair'): ")
    if entrada == 'sair':
        break
```

## Controle de Fluxo em Laços

### Break e Continue
```python
# Break: interrompe o laço
for numero in range(10):
    if numero == 5:
        break
    print(numero)

# Continue: pula iteração
for numero in range(10):
    if numero % 2 == 0:
        continue
    print(numero)  # Imprime apenas ímpares
```

### Else em Laços
```python
# Bloco else executado se laço não for interrompido
for numero in range(5):
    print(numero)
else:
    print("Laço concluído sem interrupções")
```

## Compreensão de Laços

### List Comprehension
```python
# Criação de listas com laços compactos
quadrados = [x**2 for x in range(10)]
pares = [x for x in range(10) if x % 2 == 0]
```

### Iterando Dicionários
```python
# Iteração em dicionários
usuario = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Iteração por chaves
for chave in usuario:
    print(chave)

# Iteração por valores
for valor in usuario.values():
    print(valor)

# Iteração por itens
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")
```

## Laços Aninhados
```python
# Laços dentro de laços
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

## Exercícios Propostos

### Exercício 1: Tabuada Interativa
Crie um programa que:
- Solicite um número ao usuário
- Gere a tabuada completa deste número
- Permita que o usuário escolha continuar ou sair
- Mostre estatísticas ao final (número de operações, etc.)

### Exercício 2: Validação de Senha
Desenvolva um sistema que:
- Peça ao usuário para criar uma senha
- Tenha requisitos mínimos (comprimento, caracteres especiais)
- Use laços para validação
- Dê feedback específico sobre cada requisito
- Permita múltiplas tentativas

### Exercício 3: Análise de Série Numérica
Faça um programa que:
- Receba uma série de números do usuário
- Permita entrada até um valor de parada
- Calcule:
  * Soma total
  * Média
  * Maior e menor valor
  * Quantidade de números pares e ímpares

## Diferenças para Shellscript
1. Sintaxe mais limpa e legível
2. Não precisa de `do` e `done`
3. `range()` substitui `{1..5}`
4. Mais opções de iteração
5. Compreensão de listas (list comprehension)

## Dicas Importantes
- Use `break` e `continue` com parcimônia
- Prefira list comprehension para operações simples
- Lembre-se da indentação no Python
- Explore métodos de iteração em diferentes tipos de dados

## Próxima Aula
Na próxima aula, abordaremos:
- Funções em Python
- Definição e chamada de funções
- Parâmetros e retornos
- Escopo de variáveis

Alguma dúvida sobre laços em Python?
