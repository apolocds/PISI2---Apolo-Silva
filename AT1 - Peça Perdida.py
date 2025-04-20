# A primeira linha contém um inteiro N (2 ≤ N ≤ 1.000)
# recebe o valor de N que representa o número de peças obtidas
N = int(input("Insira o valor de N: "))

# A segunda linha contém N - 1 inteiros numerados de 1 a N (sem repetições)
# trasforma a entrada do usuário numa lista de números inteiros onde cada um dos números representa uma peça diferente
numeros = list(map(int, input(f"Liste os números de 1 à {N} sem repeticões: ").split()))

# calcula a soma que representa o número ideal do total de peças do quebra cabeça
soma_total = N * (N + 1) // 2  # //2 pra garantir que o resultado seja inteiro

# soma dos números da lista
soma_parcial = sum(numeros)

# a diferença é o número que está faltando
falta = soma_total - soma_parcial

print(f"\nO número que está faltando é {falta}")
