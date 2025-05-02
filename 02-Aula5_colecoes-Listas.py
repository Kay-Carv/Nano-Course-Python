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
# %%
