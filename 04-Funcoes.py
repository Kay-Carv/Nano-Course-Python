#  Funções

# %%
# -------------------------------------------------------------------------# 
# Funções sem parametros
# -------------------------------------------------------------------------# 

#Função que calcula a velocidade média
def calcular_velocidade_media():
    velocidade_media = distancia/tempo
    print(f"A velocidade média é {velocidade_media}")

#aqui começa o programa principal
#solicitar distância e tempo
distancia = float(input("Digite a distância percorrida "))
tempo = float(input("Digite o tempo da viagem "))
calcular_velocidade_media()

# %%
# -------------------------------------------------------------------------# 
# Funções com parâmetros
# -------------------------------------------------------------------------# 

#Função que calcula a velocidade média
def calcular_velocidade_media(distancia: float, tempo: float):     # Algo interessante aqui, é possível transformar os parametros para float, string, int, etc...como se fossem dicionário
    velocidade_media = distancia/tempo
    print(f"A velocidade média é {velocidade_media}")

#aqui começa o programa principal
#solicitar distância e tempo
distancia = float(input("Digite a distância percorrida "))
tempo = float(input("Digite o tempo da viagem "))

calcular_velocidade_media(distancia, tempo)

# %%
# -------------------------------------------------------------------------# 
# Funções com parâmetros padrão
# -------------------------------------------------------------------------# 

#Função
def calcularVelocidadeMedia(distancia: float, tempo:float, unidade_medida="km/h"): # Atribui um valor de tipagem padrão, "km/h", isso é uma boa prática pois outros devs podem entendem de maneira mais facilmente
    velocidade_media = distancia/tempo
    print(f"A velocidade média é {velocidade_media} {unidade_medida}")


calcularVelocidadeMedia(360, 3)
calcularVelocidadeMedia(200, 10, "m/s") #chamada passando o valor "m/s" para o argumento unidade_media


# -------------------------------------------------------------------------# 
# Funções com argumentos variáveis (*ARGS)
# -------------------------------------------------------------------------# 

def exibe_promocao(*clientes):  # Com um "*" a gente informa para a função que teremos vários argurmentos
    for cliente in clientes:
        print(f"Olá, {cliente}!\nQueremos te avisar que o Notebook ACER nitro V15 está em promoção!")


exibe_promocao("Kayque Carvalho", "Bianca Jesus", "Ana Paula")  

print()

def exibe_promocao(*clientes):  # Com um "*" a gente informa para a função que teremos vários argurmentos
    for cliente in clientes:
        print(f"Olá, {cliente}!\nQueremos te avisar que o Notebook ACER nitro V15 está em promoção! EX usando: {lista}")

lista = ["Kayque Carvalho", "Bianca Jesus", "Ana Paula"]

exibe_promocao(*lista) # Preciso usar "*"

# %%

# -------------------------------------------------------------------------# 
# Funções com argumentos variáveis nomeados (**KWARGS)
# -------------------------------------------------------------------------# 


# KEYWORD ARGS = argumentos com palavra-chave e valor

def exibe_ficha(**dados):
    print(f"Dicionário:\n{dados}")
    print("\n----FICHA----\n")
    for chave, valor in dados.items():
        print(f"{chave.upper()} -- {valor}")

ficha_cliente = {
    "nome":"Francisco Vargas",
    "estado civil":"casado",
    "idade":"35",
    "filhos": True
}

# Utilizando o dicionário
exibe_ficha(**ficha_cliente)

# Criando chave e valor em uma variável
exibe_ficha(nome="Binca Jesus", estado_civil="solteiro(a)")
exibe_ficha() # Retorna chave vazia

# %%

# -------------------------------------------------------------------------# 
# Funções com return
# -------------------------------------------------------------------------# 

# Return serve para armazenar/criar dados para devolver um resultado de acordo com a necessidade

def soma(a, b):
    resultado = a + b
    return resultado
valor1 = int(input("Informe o prieiro valor que deseja somar "))
valor2 = int(input("Informe o segundo valor que deseja somar "))
resposta = soma(valor1, valor2)
print(f"A variável resposta recebeu o return da função soma() e agora contém: {resposta}")
print(f"A função soma() está sendo chamada dentro deste print para os valores 10 e 15 e retornou: {soma(10, 15)}")

# %%

# -------------------------------------------------------------------------# 
# Um script de funções
# -------------------------------------------------------------------------# 


# Função calcula média de 
def calcular_velocidade_media(distancia:float, tempo:float, unidade_medida="km/h"):
    if tempo == 0:
        return
    velocidade_media = distancia / tempo
    return f"{velocidade_media} {unidade_medida}"

# Função Converte temperatura
def converter_temperatura(temperatura:float, unidade_medida="celsius"):
    if unidade_medida == "celsius":
        return temperatura * 1.8 + 32
    elif unidade_medida == "fahrenheit":
        return (temperatura - 32) / 1.8
    else:
        return 0
    
def exibir_menu():
    print("MENU")
    print("1 - Calcular a velocidade média ")
    print("2 - Converter a temperatura ")
    print("3 - Sair")

# Função dentro de função
def aluno_de_fisica():
    op = 0
    while op != 3:
        exibir_menu()
        op = int(input("Informe a opção desejada: "))
        if op == 1:
            distancia_percorrida = float(input("Informe a distância: "))
            tempo_viagem = float(input("Iforme o tempo da viagem: "))
            # medida = input("Informe a unidade de medida: ")
            print(f"\nA velocidade média é {calcular_velocidade_media(distancia_percorrida, tempo_viagem)}\n")
        elif op == 2:
            temperatura_informada = float(input("Informe a temperatura que deseja converter: "))
            medida = input("A temperatura informada está em celsius ou fahrenheit")
            print(f"\nO resultado da conversão é {converter_temperatura(temperatura_informada, medida)}\n")
        elif op == 3:
            print("\nSaindo do sistema...\n")
            break
        else:
            print("Opção inválida!")

aluno_de_fisica()
# Também é possivel fazer essa requisição de um função através de um arquivo externo

# import nome_do_arquivo

#nome_do_arquivo.aluno_de_fisica()

# Dessa forma você usa arquivos externos para rodar o código presente dentro desse arquivo
# OBS: evite que o arquivo esteja renomeado com "-" e também evite começando com números   


# %%

# -------------------------------------------------------------------------# 
# Documentar funções
# -------------------------------------------------------------------------# 

def somar(a:float, b:float):
    """Recebe dois argumentos, a e b, tipo float e realiza a soma.
     Retorna o resultado no formato float"""  # Exemplo de documentação do que a função faz
    return a + b

print(f"Chamando o método doc para ler a documentação: {somar.__doc__}") # Para consutar essa documentação é possivel usar o método __doc__
print(f"Chamando a função help para ler a documentação: {help(somar)}")  # Também é possível usar help(função)