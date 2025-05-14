# %%

"""defaultdict ótimo para atribuir valor padrão para chaves que não foram cadastradas/não existem em dicionário """

# Importando sub-classe do dicionário
from collections import defaultdict

dicionario_lista = defaultdict(list)

dicionario_lista["produto"] = "Macbook Pro"
dicionario_lista["marca"] = "Apple"

print(dicionario_lista["preco"]) # Quando a gente usa uma chave que não existe o defaultdic cria um valor padrão para chaves que não existe

print(dicionario_lista)


# ATRIBUINDO VALOR PADRÃO PRA CHAVE INEXISTENTE
def funcao_exemplo():
    return "INEXISTENTE"


dicionario_funcao = defaultdict(funcao_exemplo)

dicionario_funcao["PRODUTO"] = "Macbook Pro"
dicionario_funcao["MARCA"] = "Apple"

print(dicionario_funcao)
print(dicionario_funcao["PRECO"]) # Quando a gente usa uma chave que não existe o defaultdic cria um valor padrão para chaves que não existe

print(dicionario_funcao)


# %%

# Usando função LAMBDA para atribuir valor padrão

dicionario_lambda = defaultdict(lambda: "Não disponível")

dicionario_lambda["PRODUTO"] = "Macbook Pro"
dicionario_lambda["MARCA"] = "Apple"

print(dicionario_lambda)
print(dicionario_lambda["PRECO"]) # Quando a gente usa uma chave que não existe o defaultdic cria um valor padrão para chaves que não existe

print(dicionario_lambda)
# %%

# OrderedDict

"""A sub-classe OrderecDict se recorda das posições de indice Chave dos dicionários

A solução serve para que os elementos respeitem sempre a mesma ordem da qual foram inseridos

"""

from collections import OrderedDict

dicionario_ordenado = OrderedDict()

print(dicionario_ordenado)

# Adiciona chaves e valor

dicionario_ordenado["NOME"] = "SamartPhone Galax"
dicionario_ordenado["MARCA"] = "Samsung"
dicionario_ordenado["MODELO"] = "S25 ultra"

# Verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f"Chave:{chave}  Valor:{valor}")

# Alterando um item

print("\nApós alterar um item\n")

dicionario_ordenado["MARCA"] = "Apple"

for chave, valor in dicionario_ordenado.items():
    print(f"Chave: {chave}   Valor: {valor}")

"""O que aconteceu aqui foi que a implementação de um novo elemento não alterou a ordem
 de como o dicionário é escrito"""

# Remover um elemento

print("\nApós remover uma chave \n")

dicionario_ordenado.pop("MARCA")

for chave, valor in dicionario_ordenado.items():
    print(f"Chave: {chave}    Valor: {valor}")

## Após eu remover a chave marca e adicionar de novo...A ordem vai se manter?

print("\nApós reinserir\n")

dicionario_ordenado["MARCA"] = "Samsung"


for chave, valor in dicionario_ordenado.items():
    print(f"Chave: {chave}    Valor: {valor}")

    # A ordem foi alterada....

"""Usado apenas em um cenário na onde é necessario manter a ordem das chaves"""

# %%



# namedtuple

"""Permite a criação de nomes para cada um dos dados"""

from collections import namedtuple

Produto = namedtuple("Produto", ["nome", "marca", "preco"]) #Criação do novo tipo,  Ao criar um novo objeto que seja do tipo Produoto, fornecemos os valores para os três campos 
novo_produto = Produto("Ipad", "Apple", 2499.99)

print(f"Criamos o objeto chamado novo_produto, usando como tipo Produto. Ao exibirmos este objeto temos: \n{novo_produto}")

#iteração
print("\nComo a namedtuple ainda é uma tuple, podemos iterá-la: ")
for valor in novo_produto:
    print(valor)
#desempacotamento
x, y, z = novo_produto    # algo bem semelhante com as listas e tuplas dentro das funções, já que temos vários itens dentro
print(f"\nTambém foi possível desempacotar os valores de novo_produto nas variáveis X={x}, Y={y} e Z={z}")

novo_produto2 = Produto("Mouse M900 pro", "Delux", "245.98")
print("\n ",novo_produto2)
a, b, c = novo_produto2

print(f"\n{a}\n{b}\n{c}")

# %%



# deque
"""
A estrutura deque permite inserção e remoção de elementos
tanto no início quanto no fim da fila, de forma eficiente.
É útil para filas, pilhas, e buffers cíclicos.
"""

from collections import deque

"""
Exemplo de uso da estrutura deque:
Uma fila de tarefas onde podemos adicionar e remover tarefas do início ou do fim.
"""

# Criando a deque com tarefas iniciais
tarefas = deque(["Lavar louça", "Estudar Python", "Ir ao mercado"])
print("Fila inicial:", tarefas)

# Adicionando tarefas ao fim e ao início
tarefas.append("Fazer exercícios")        # fim
tarefas.appendleft("Tomar café da manhã") # início
print("\nApós adicionar tarefas:", tarefas)

# Removendo tarefas do início e do fim
tarefas.pop()       # Remove do fim
tarefas.popleft()   # Remove do início
print("\nApós remover tarefas:", tarefas)

# Adicionando várias tarefas ao fim e ao início
tarefas.extend(["Ler livro", "Fazer almoço"])
tarefas.extendleft(["Arrumar cama", "Escovar os dentes"])  # Ordem invertida
print("\nApós adicionar várias tarefas:", tarefas)

# Rotacionando a fila de tarefas
tarefas.rotate(2)
print("\nApós girar tarefas 2 posições para a direita:", tarefas)

tarefas.rotate(-3)
print("\nApós girar tarefas 3 posições para a esquerda:", tarefas)


# %%
"""
| Código de Exemplo                                                       | O que faz                                                                | Resultado esperado                                                        |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `tarefas = deque(["Tomar café", "Estudar Python", "Ir ao mercado"])`    | Cria a fila com três tarefas iniciais.                                   | `deque(["Tomar café", "Estudar Python", "Ir ao mercado"])`                |
| `tarefas.append("Ler um livro")`                                        | Adiciona **"Ler um livro"** ao final da fila.                            | `deque([... "Ir ao mercado", "Ler um livro"])`                            |
| `tarefas.appendleft("Arrumar a cama")`                                  | Adiciona **"Arrumar a cama"** no início da fila.                         | `deque(["Arrumar a cama", ...])`                                          |
| `tarefas.pop()`                                                         | Remove o último item da fila.                                            | Remove o último (ex: **"Ler um livro"**)                                  |
| `tarefas.popleft()`                                                     | Remove o primeiro item da fila.                                          | Remove o primeiro (ex: **"Arrumar a cama"**)                              |
| `tarefas.extend(["Estudar", "Trabalhar"])`                              | Adiciona várias tarefas ao final da fila.                                | `deque([... "Ir ao mercado", "Estudar", "Trabalhar"])`                    |
| `tarefas.extendleft(["Escovar dentes", "Lavar rosto"])`                 | Adiciona várias tarefas ao início (em ordem invertida).                  | `deque(["Lavar rosto", "Escovar dentes", ...])`                           |
| `tarefas.rotate(1)`                                                     | Move os itens 1 posição à direita.                                       | O último item vai para o início.                                          |
| `tarefas.rotate(-2)`                                                    | Move os itens 2 posições à esquerda.                                     | Os dois primeiros itens vão para o final.                                 |
"""