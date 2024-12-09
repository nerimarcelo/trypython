# Aula 2: Listas e Manipulação de Dados em Python

## Objetivos da Aula
- Entender o conceito de listas em Python
- Aprender operações básicas com listas
- Explorar métodos de manipulação de listas
- Comparar com manipulação de arrays no shellscript

## Listas em Python: Fundamentos

### Criação de Listas
```python
# Formas de criar listas
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
lista_mista = [1, "texto", 3.14, True]
lista_vazia = []
```

### Acessando Elementos
```python
# Indexação (similar ao shellscript)
print(frutas[0])        # Primeiro elemento
print(frutas[-1])       # Último elemento
print(frutas[1:3])      # Fatiar lista (slice)
```

### Modificando Listas
```python
# Adicionar elementos
frutas.append("uva")        # Adiciona no final
frutas.insert(1, "manga")   # Insere em posição específica

# Remover elementos
frutas.remove("banana")     # Remove primeiro elemento encontrado
del frutas[1]               # Remove por índice
ultimo = frutas.pop()       # Remove e retorna último elemento
```

## Comparação com Shellscript

### Shellscript (Arrays)
```bash
# Criação de array no shellscript
frutas=("maçã" "banana" "laranja")

# Acessando elementos
echo ${frutas[0]}        # Primeiro elemento
echo ${frutas[-1]}       # Último elemento
```

### Diferenças Principais
1. Listas em Python são mais flexíveis
2. Podem conter tipos diferentes de dados
3. Possuem métodos embutidos mais poderosos
4. Indexação mais simples e intuitiva

## Operações Avançadas

### Ordenação
```python
# Ordenar listas
numeros = [3, 1, 4, 1, 5, 9, 2]
numeros.sort()           # Ordena in-place
numeros_ordenados = sorted(numeros)  # Retorna nova lista
```

### Compreensão de Listas
```python
# Criar listas de forma compacta
quadrados = [x**2 for x in range(10)]
pares = [x for x in range(10) if x % 2 == 0]
```

### Operações com Múltiplas Listas
```python
# Juntar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
combinada = lista1 + lista2

# Multiplicar lista
repetida = lista1 * 3
```

## Métodos Úteis de Listas

### Contagem e Busca
```python
# Verificar existência
print("maçã" in frutas)     # Retorna True/False
print(frutas.count("maçã")) # Conta ocorrências
print(frutas.index("maçã")) # Encontra índice
```

### Outras Operações
```python
# Tamanho da lista
print(len(frutas))

# Limpar lista
frutas.clear()

# Copiar lista
nova_lista = frutas.copy()
```

## Exercícios Propostos

### Exercício 1: Gerenciamento de Lista de Compras
Crie um programa que permita:
- Adicionar itens à lista de compras
- Remover itens da lista
- Listar todos os itens
- Verificar se um item existe na lista

### Exercício 2: Análise de Notas
Desenvolva um script que:
- Receba uma lista de notas de um aluno
- Calcule a média das notas
- Identifique a maior e menor nota
- Informe quantas notas estão acima da média

### Exercício 3: Transformação de Dados
Crie um programa que:
- Tenha uma lista inicial de números
- Gere uma nova lista com os números:
  * Multiplicados por 2
  * Apenas números pares
  * Ordenados em ordem decrescente

## Dicas para Resolução
- Use os métodos de lista apresentados
- Preste atenção na sintaxe do Python
- Teste cada parte do código separadamente
- Não hesite em usar print() para depuração

Alguma dúvida sobre listas em Python?