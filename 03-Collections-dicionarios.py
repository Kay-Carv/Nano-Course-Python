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
