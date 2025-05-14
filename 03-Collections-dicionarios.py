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
