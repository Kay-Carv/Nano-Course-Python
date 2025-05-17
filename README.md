# Nano Course: Python Development - FIAP

Olá, me chamo Kayque Carvalho e atualmente estou cursando Engenharia de Software na **FIAP** 
(Faculdade de Informática e Administração Paulista), a linguagem de programação **`Python`** é uma das que eu mais gosto, logo decidi fazer um curso de **Python Development** oferecido pela faculdade.

# Objetivo do repositório

Esse repositório tem como objetivo **documentar** os conteúdos de python vistos no **Nano Course de Python Development** feito na **FIAP**.

# Métodos do python

Métodos são funções associadas a objetos. Eles realizam ações específicas sobre esses objetos e são chamados usando a sintaxe ``objeto.método()``. Em **Python**, diferentes tipos de dados — como **listas, dicionários e sets(conjuntos)** — possuem seus próprios métodos, que permitem manipular ou consultar seus conteúdos de forma prática e eficiente.

---

## Listas

Listas são estruturas ordenadas e mutáveis que armazenam uma sequência de elementos. Permitem duplicatas e acesso por índice.

| Código de Exemplo                                 | O que faz                                                                     | Resultado esperado                               |
|---------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------|
| `lista = ['Bianca', 'Carol', 'Ana', 'Bianca']`    | Cria uma lista com quatro nomes, dois deles repetidos.                        | `['Bianca', 'Carol', 'Ana', 'Bianca']`           |
| `lista.append('João')`                            | Adiciona **João** no final da lista.                                          | `['Bianca', 'Carol', 'Ana', 'Bianca', 'João']`   |
| `lista.index('Ana')`                              | Retorna a posição da primeira ocorrência de **Ana**.                          | `2`                                              |
| `lista.insert(1, 'Lucas')`                        | Insere **Lucas** na posição 1.                                                | `['Bianca', 'Lucas', 'Carol', 'Ana', 'Bianca']`  |
| `lista.pop()`                                     | Remove o último elemento.                                                     | Remove **Bianca**                                |
| `lista.pop(2)`                                    | Remove o item na posição 2.                                                   | Remove **Carol**                                 |
| `lista.count('Bianca')`                           | Conta quantas vezes **Bianca** aparece.                                       | `2`                                              |
| `lista.sort()`                                    | Ordena a lista em ordem alfabética.                                           | `['Ana', 'Bianca', 'Bianca', 'Carol']`           |
| `lista.sort(reverse=True)`                        | Ordena a lista em ordem alfabética reversa.                                   | `['Carol', 'Bianca', 'Bianca', 'Ana']`           |
| `lista.reverse()`                                 | Inverte a ordem da lista.                                                     | Ordem da lista é invertida.                      |
| `lista.remove('Ana')`                             | Remove a primeira ocorrência de **Ana**.                                      | `['Bianca', 'Carol', 'Bianca']`                  |

---

## Tuplas

Tuplas são imutáveis, ou seja, não podem ser alteradas após serem criadas. São úteis para representar conjuntos fixos de valores.

| Código de Exemplo                            | O que faz                                                       | Resultado esperado               |
|----------------------------------------------|------------------------------------------------------------------|----------------------------------|
| `coordenadas = (10.0, 20.0)`                 | Cria uma tupla com duas coordenadas.                            | `(10.0, 20.0)`                   |
| `coordenadas[0]`                             | Acessa o primeiro valor da tupla.                               | `10.0`                          |
| `len(coordenadas)`                           | Retorna o tamanho da tupla.                                     | `2`                             |
| `'x' in coordenadas`                         | Verifica se `'x'` está presente na tupla.                       | `False`                         |
| `coordenadas + (30.0,)`                      | Cria nova tupla adicionando valor. Tuplas são imutáveis!        | `(10.0, 20.0, 30.0)`             |

---

## Sets

Sets (ou conjuntos) são coleções não ordenadas de elementos únicos. São ideais para eliminar duplicatas e realizar operações matemáticas como união e interseção.

| Código de Exemplo                                                    | O que faz                                                                   | Resultado esperado                       |
|------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------|
| `conjunto = set([1, 2, 3, 2, 1])`                                      | Cria um set sem elementos duplicados.                                       | `{1, 2, 3}`                              |
| `conjunto.add(4)`                                                     | Adiciona o número 4.                                                        | `{1, 2, 3, 4}`                           |
| `conjunto.remove(2)`                                                  | Remove o número 2 (erro se não existir).                                    | `{1, 3, 4}`                              |
| `conjunto.discard(5)`                                                 | Tenta remover o número 5 (não dá erro se não existir).                      | `{1, 3, 4}`                              |
| `conjunto2 = {3, 4, 5}`                                                | Cria outro set para operações de conjunto.                                  | `{3, 4, 5}`                              |
| `conjunto.union(conjunto2)`                                           | Une os dois sets.                                                           | `{1, 3, 4, 5}`                           |
| `conjunto.intersection(conjunto2)`                                    | Retorna a interseção (elementos em comum).                                  | `{3, 4}`                                 |
| `conjunto.symmetric_difference(conjunto2)`                             | Elementos que estão em um ou outro, mas não nos dois.                       | `{1, 5}`                                 |
| `conjunto.issubset(conjunto2)`                                        | Verifica se conjunto está contido em conjunto2.                             | `False`                                  |
| `conjunto.isdisjoint({10, 11})`                                        | Verifica se não há elementos em comum.                                      | `True`                                   |

---

## Dicionários

Dicionários armazenam dados em pares `chave: valor`.

| Código de Exemplo                                               | O que faz                                                       | Resultado esperado                               |
|------------------------------------------------------------------|------------------------------------------------------------------|--------------------------------------------------|
| `aluno = {"nome": "Ana", "idade": 22}`                           | Cria um dicionário com duas informações.                         | `{"nome": "Ana", "idade": 22}`                   |
| `aluno["nome"]`                                                  | Acessa o valor da chave `"nome"`.                                | `"Ana"`                                          |
| `aluno.get("curso", "Não definido")`                             | Acessa valor de `"curso"` ou retorna valor padrão.               | `"Não definido"`                                 |
| `aluno["idade"] = 23`                                            | Atualiza o valor da chave `"idade"`.                             | `{"nome": "Ana", "idade": 23}`                   |
| `aluno.update({"curso": "Python"})`                              | Adiciona a chave `"curso"` ao dicionário.                         | `{"nome": "Ana", "idade": 23, "curso": "Python"}`|
| `list(aluno.keys())`                                             | Retorna uma lista com as chaves.                                 | `["nome", "idade", "curso"]`                     |
| `list(aluno.values())`                                           | Retorna uma lista com os valores.                                | `["Ana", 23, "Python"]`                          |
| `list(aluno.items())`                                            | Retorna uma lista de tuplas (chave, valor).                      | `[("nome", "Ana"), ("idade", 23), ...]`          |
| `aluno.pop("idade")`                                             | Remove a chave `"idade"`.                                        | Remove idade e retorna `23`                      |
| `aluno.clear()`                                                  | Remove todos os elementos do dicionário.                         | `{}`                                             |

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

---

## Tópicos avançados

![Status](https://img.shields.io/badge/Documentacao%20de%20topicos%20Avancados-%20Status:em%20desenvolvimento-yellow)
