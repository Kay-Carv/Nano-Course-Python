# %%
# solicite um valor para o usuário
# Com base nesse valor, crie uma estrutura de piramide de '*' crescente até o valor do usuário 
# e que descreça até chegar ao começo

valor_user = int(input("Digite o valor máximo que a pirâmide vai atingir: "))

for i in range(1, valor_user + 1):
    print('*' * i)

for i in range(valor_user -1, 0, -1):
    print('*' * i)



# %%

# Criando um número aleatório para ser acertado
import random

senha = random.randint(1, 10)
tentativa = 1
resposta = int(input('Adivinhe o número entre 1 a 10: '))

while resposta != senha:
    print(senha)
    tentativa += 1
    resposta = int(input('Adivinhe o número entre 1 a 10: '))

print(f'\n O número secreto era {senha}! Você acertou com {tentativa} tentativa(s)')

# %%
# Definindo range em contador
# Range (valor inicial, valor final, de quanto em quanto)

for contador in range(10, 100, 2):
    print(contador) # Vai somar de 2 em 2 até 98
    if contador == 60: #Quebrando o 
        break

# %%

# Calculo fatorial de um número, ordem descrecente ...5 * 4 *3*2*1 ignorando o 0

numero = int(input('Digite o número para descobrir o seu fatorial'))
fatorado = numero

for i in range(fatorado -1, 0, -1):
    fatorado = fatorado * i

print(f'O fatorial do número {numero}! é igual a {fatorado}')

# %%

# Calculo fatorial de um número, ordem crescente EX: 1 * 2 *3 *4...

numero = int(input('Digite o número para descobrir o seu fatorial'))
fatorado = numero

for i in range(1, fatorado, 1):
    fatorado = fatorado * i

print(f'O fatorial do número {numero}! é igual a {fatorado}')


# %%

# Juntando todos os conhecimentos em uma única estrutura

import random

opcao = 0

while opcao != 4:
    print('\n','*' * 15)
    print('\n\t1 - Receber um número aleatóeio de 1 a 100')
    print("\n\t2 - Fatoração de um número!")
    print("\n\t3 - Gerar uma piramide com '*'")
    print("\n\t4 - Sair")
    print('\n','*' * 15)
    opcao = int(input('Escolha uma opção de 1 a 4: '))

    if opcao == 1:
        print("\nO número aleatório gerado é: ", random.randint(0, 100))

    elif opcao == 2:
        valor = int(input("Digite um número para ser fatorado: "))
        fat = valor

        for i in range(1, fat, 1):
            fat = i * fat
        
        print(f"\n O fatorial do número {valor}! é igual a {fat}")

    elif opcao == 3:
        max_piramide = int(input("Digite o valor máximo da pirâmide: "))

        for i in range(1, max_piramide +1):
            print('*' * i)
        
        for i in range(max_piramide - 1, 0, -1):
            print('*' * i)
            
    elif opcao == 4:
        print("Saindo do sistema...")
        break

    else:
        print("\nDigite um valor válido entre 1 a 4: ")
