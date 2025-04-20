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
