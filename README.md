# Nano Course: Python Development - FIAP

Olá, me chamo Kayque Carvalho e atualmente estou cursando Engenharia de Software na **FIAP** 
(Faculdade de Informática e Administração Paulista), a linguagem de programação **`Python`** é uma das que eu mais gosto, logo decidi fazer um curso de **Python Development** oferecido pela faculdade.

# Objetivo do repositório

Esse repositório tem como objetivo **documentar** os conteúdos de python vistos no **Nano Course de Python Development** feito na **FIAP**.

# Métodos do python


## Listas


| Método                          | Efeito                                                                 |
|---------------------------------|------------------------------------------------------------------------|
| `lista.append(elemento)`        | Adiciona um elemento no final da lista.                               |
| `lista.index(elemento)`         | Retorna o índice de um determinado elemento.                          |
| `lista.insert(posicao, item)`   | Insere um elemento em uma posição específica, fazendo com que os elementos posteriores a ele recebam novos índices. |
| `lista.pop()`                   | Remove o último elemento de uma lista.                                |
| `lista.pop(posicao)`            | Remove o elemento que está em uma posição específica da lista.        |
| `lista.count("item")`           | Retorna o número de vezes que um elemento aparece na lista.           |
| `lista.sort()`                  | Ordena a lista em ordem crescente.                                    |
| `lista.sort(reverse=True)`      | Ordena a lista em ordem decrescente.                                  |
| `lista.reverse()`               | Inverte a ordem dos elementos de uma lista.                           |
| `lista.remove(item)`            | Remove um item da lista.                                              |

## Tuplas


## Sets

| Método                                | Descrição                                                                 |
|---------------------------------------|---------------------------------------------------------------------------|
| `set.symmetric_difference(set1, set2)`| Retona um set com os elementos que não se repetem em dois sets.          |
| `set.union(set1, set2, ...)`          | Retorna um set contendo os elementos dos sets indicados                   |
| `set.intersection(set1, set2, ...)`   | Retorna um set com os elementos que existem em todos os sets indicados    |
| `set.isdisjoint(set2)`                | Retorna verdadeiro se os dois sets contêm elementos diferentes e falso se algum dos elementos for igual. |
| `set.issubset(set2)`                  | Retorna verdadeiro se o set está contido em outro.                        |
| `set.issuperset(set2)`                | Retorna verdadeiro se um set contém outro set.                            |
| `set.clear()`                         | Remove todos os elementos do set.                                         |
| `set.copy()`                          | Retorna uma cópia do set.                                                 |
| `set.pop()`                           | Remove um elemento aleatório do set.                                      |
| `set.remove()`                        | Remove um elemento do set e retorna um erro caso o elemento não exista.   |
| `set.discard()`                       | Remove um elemento do set e não retorna um erro caso o elemento não exista. |


## Dicionários

| Método                                  | Efeito                                                                 |
|-----------------------------------------|------------------------------------------------------------------------|
| `dicionario.get(chave)`                 | Retorna o valor associado a uma chave específica.                      |
| `dicionario.values()`                   | Retorna uma lista com os valores do dicionário.                        |
| `dicionario.keys()`                     | Retorna uma lista de chaves do dicionário.                             |
| `dicionario.items()`                    | Retorna uma lista de tuplas contendo chave e valor.                    |
| `dict.fromkeys(chaves, valor)`          | Retorna um dicionário com base nas chaves especificadas. Pode ou não atribuir um valor fornecido. |
| `dicionario.setdefault(chave, valor)`   | Retorna o valor de uma determinada chave. Se a chave não existir, é criada com valor None ou o valor informado. |
| `dicionario.update({chave: valor})`     | Atualiza o dicionário com base na chave e no valor fornecidos.         |
| `dicionario.copy()`                     | Retorna uma cópia do dicionário.                                       |
| `dicionario.pop(chave) `                | Remove um item do dicionário com base na chave.                        |
| `dicionario.popitem()`                  | Remove a última chave e valor inserida no dicionário.                  |
| `dicionario.clear()`                    | Remove todos os elementos do dicionário.                               |

### Deque
A estrutura deque permite inserção e remoção de elementos
tanto no início quanto no fim da fila, de forma eficiente.
É útil para filas, pilhas, e buffers cíclicos.
```
from collections import deque
```

Exemplo de uso da estrutura deque:
Uma fila de tarefas onde podemos adicionar e remover tarefas do início ou do fim.

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
