# Listas de tarefas

# %%
# Exemplos de algumas funcionalidades das listas

lista = [12, 15.5, "string"]

print(type(lista))

# Inserindo elemento na lista
lista.append("Texto que vai ser adicionado no final da lista")

print(lista)

# Como exibir através do inidice
print(lista[0])         # Primeiro indice
print(lista[-1])        # Mostra o último indice
print(lista[0:3])       # Vai exibir do primeito indice até <3

# Exibindo cada elemento da lista como se fosse \n
for valor in lista:
    print(valor)

# Removendo um valor da lista
lista.pop()         # Remove o último indice da lista
print(lista)

lista.remove(12) # Remove o exato valor da lista
print(lista)

# Tamanho da lista
print("A lista possui", len(lista), "elemento(s)")

# %%
# Criando um Programa para calcular a quantidade de calorias de refeições feitas no dia 
calorias = []
resposta = ""

while resposta.lower() != 'não' and resposta.lower() != 'nao':
    caloria = int(input("Quantas calorias você consumiu nessa refeição?\nR: "))
    calorias.append(caloria)
    resposta = input("Você deseja informar as calorias de mais alguma refeição?\n R: ")



total = 0

for i,caloria in enumerate(calorias, start=1):
    print(f"\tForam consumidas '{caloria}' calorias na {i}° refeição")
    total = total + caloria

print(f"\n\tForam consumidas {total} de calorias em {len(calorias)} refeição(ões)")

media = total / len(calorias)

print(f"\tO consumo de calorias médio por qtd de refeição foi de: {media}")

# %%

# Outros exemplos 

cavaleiros_jedi = ["Obi-Wan Kenobi", "Mace Windu", "Mestre Yoda", "Luke Skywalker", "Anakin Skywalker"]
print(f"A lista original é \n{cavaleiros_jedi}")
cavaleiros_jedi.append("Mestre Yoda")    #Adiciona na lista
print(f"Após a adição do elemento Mestre Yoda utilizando o append, a lista é \n{cavaleiros_jedi}")
print(f"O índice do elemento Mace Windu é {cavaleiros_jedi.index('Mace Windu')}")   #Percorre a lista e busca o elemento descrito
cavaleiros_jedi.insert(1, "Rey")    #Insere um valor no indice 1
print(f"Após a adição do elemento Rey na posição 1 utilizando o insert, a lista é \n{cavaleiros_jedi}")
print(f"A contagem do elemento Mestre Yoda é {cavaleiros_jedi.count('Mestre Yoda')}") # Mostra em qual indice a str está
cavaleiros_jedi.pop()       # Remove o último indice
print(f"Após o uso do pop, a lista é \n{cavaleiros_jedi}")
cavaleiros_jedi.pop(0)      # Retira o valor do indice
print(f"Após o uso do pop com o índice 0, a lista é \n{cavaleiros_jedi}")
cavaleiros_jedi.reverse()   #Reverte para o estado inicial da lista
print(f"Após o uso do reverse, a lista é \n{cavaleiros_jedi}")
cavaleiros_jedi.sort() # do maior para o menor
print(f"Após o uso do sort, a lista é \n{cavaleiros_jedi}")
cavaleiros_jedi.sort()
print(f"Após o uso do sort(reverse=True), a lista é \n{cavaleiros_jedi}")

"""
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
"""
# %%

# SET (Conjuntos)


"SET (Conjuntos)"

"   Os sets são estruturas do Python que permitem armazenar diversos valores assim como as listas, mas não permite repetições. Dessa forma, eles se"
"tornam candidatos perfeitos para todos os cenários em que precisamos trabalhar com conjuntos de VALORES ÚNICOS."

"Os SETs apresentam uma estrutura parecida com as listas mas não aceitam valores iguai"

# Criar set vazio
conjunto = set()
print(type(conjunto))

# Crindo set apartir de uma lsita

lista = ['kayque', 'Francisco', 'Ana', 'kayque']


lista_set = set(lista)
print(f"\n{lista}\n{lista_set}\nO set não retornou o valor repetido '{lista[0]}'\n")


# set com valores

conjunto2 = {'Bianca', 'Carol', 'Ana', 'Bianca'}
print(conjunto2)


# Adicionando elementos

conjunto2.add("Paula")
print(conjunto2, "\n")

# Removendo elementos do set
set1 = {"Google", "Youtube", "Excel", "Docs"}
set2 = {"PorwerPoint", "Word", "Office", "Excel", "Planilhas"}

print(f"conjunto 1: {set1}")
print(f"conjunto 2: {set2}")

"Fazendo comparação entre os conjuntos"
set1.difference_update(set2)
print(f"O primeiro set agora contém {set1} pois removel os valores iguais entre os dois conjuntos")

# Remover um valor específico

set2.remove("Planilhas")
print(f"O elemento Planilhas foi removido de: {set2}")


"""Obs: se você tentar remover um elemento que não existe, vai retornar um erro, logo usamos {discard}"""


set2.discard("Google")
print(set2)

"""
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
"""