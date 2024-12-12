# Aula 3: Dicionários em Python para Programadores de Shellscript

## Objetivos da Aula
- Entender o conceito de dicionários em Python
- Comparar dicionários com estruturas de dados no shellscript
- Aprender operações básicas e avançadas com dicionários
- Explorar casos de uso práticos

## Dicionários em Python: Fundamentos

### O que são Dicionários?
Dicionários são estruturas de dados que armazenam pares de chave-valor, semelhantes a arrays associativos no shellscript.

### Criação de Dicionários
```python
# Formas de criar dicionários
usuario = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "São Paulo"
}

# Construtor dict()
contato = dict(telefone="1234-5678", email="joao@exemplo.com")
```

### Comparação com Shellscript
- Shellscript (Arrays Associativos):
```bash
declare -A usuario=(
    ["nome"]="João Silva"
    ["idade"]=30
    ["cidade"]="São Paulo"
)

# Acessar valor
echo ${usuario["nome"]}
```

- Python (Dicionários):
```python
print(usuario["nome"])
```

## Operações Básicas com Dicionários

### Acessando e Modificando Valores
```python
# Acessar valor
print(usuario["nome"])

# Adicionar/Modificar
usuario["profissao"] = "Programador"
usuario["idade"] = 31

# Método get() (seguro)
idade = usuario.get("idade", "Idade não definida")

# Remover elementos
del usuario["cidade"]
idade_removida = usuario.pop("idade", None)
```

### Métodos Úteis
```python
# Verificar existência de chave
print("nome" in usuario)

# Obter todas as chaves e valores
print(usuario.keys())
print(usuario.values())
print(usuario.items())
```

## Iteração em Dicionários
```python
# Iterar sobre chaves
for chave in usuario:
    print(chave, usuario[chave])

# Iterar sobre itens
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")
```

## Dicionários Aninhados
```python
# Dicionários dentro de dicionários
empresa = {
    "nome": "Tech Solutions",
    "funcionarios": {
        "joao": {"cargo": "Desenvolvedor", "salario": 5000},
        "maria": {"cargo": "Gerente", "salario": 7000}
    }
}

# Acessar valores aninhados
print(empresa["funcionarios"]["joao"]["cargo"])
```

## Métodos Avançados

### Cópia de Dicionários
```python
# Cópia rasa
novo_usuario = usuario.copy()

# Cópia profunda (nested)
import copy
usuario_profundo = copy.deepcopy(usuario)
```

### Mesclar Dicionários
```python
# Python 3.9+
usuario_completo = usuario | contato

# Método update()
usuario.update(contato)
```

## Exercícios Propostos

### Exercício 1: Gerenciamento de Inventário
Crie um programa de gerenciamento de inventário que permita:
- Adicionar produtos com nome, quantidade e preço
- Atualizar quantidade de produtos
- Remover produtos
- Listar todos os produtos
- Calcular valor total do inventário

### Exercício 2: Sistema de Cadastro
Desenvolva um sistema de cadastro que:
- Permita cadastrar pessoas com múltiplas informações
- Possibilite busca por diferentes campos
- Imprima informações formatadas
- Valide a existência de campos antes de acessá-los

### Exercício 3: Processamento de Logs
Crie um programa que:
- Simule processamento de logs
- Agrupe logs por tipo de evento
- Conte ocorrências de cada tipo de evento
- Identifique eventos mais frequentes

## Dicas para Resolução
- Use métodos de dicionário como `.get()` para segurança
- Explore iteração com `.items()`
- Utilize tratamento de exceções para entradas inválidas
- Teste diferentes formas de acessar e modificar dicionários

## Diferenças para Shellscript
1. Mais flexível que arrays associativos do bash
2. Métodos embutidos poderosos
3. Suporte a estruturas aninhadas
4. Tipagem dinâmica

## Próxima Aula
Na próxima aula, abordaremos:
- Funções em Python
- Passagem de parâmetros
- Escopo de variáveis
- Funções lambda

Alguma dúvida sobre dicionários em Python?
