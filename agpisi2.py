import random

import time

NUM_BITS = 5
TAM_POP = 6
MAX_X = 2 ** NUM_BITS - 1  # 31
F_MAX = MAX_X ** 2         # 961
TAXA_MUTACAO = 0.1
MAX_GERACOES = 99

random.seed(int(time.time()))
print(f"Seed utilizada: {int(time.time())}")

def pop_inicial():
    return [random.randint(1, MAX_X) for _ in range(TAM_POP)]

def avaliar(individuo):
    return individuo ** 2
 
def roleta(populacao):
    aptidoes = [avaliar(ind) for ind in populacao]
    total = sum(aptidoes)
    ponto = random.uniform(0, total)
    soma = 0
    for ind, apt in zip(populacao, aptidoes):
        soma += apt
        if soma >= ponto:
            return ind
    return populacao[-1]

def crossover(pai1, pai2):
    bin1 = format(pai1, f'0{NUM_BITS}b')
    bin2 = format(pai2, f'0{NUM_BITS}b')
    filhos = []
    for ponto in [1, 2, 4]:
        filho1 = int(bin1[ponto:] + bin2[:ponto], 2)
        filho2 = int(bin2[ponto:] + bin1[:ponto], 2)
        filhos.extend([filho1, filho2])
    return filhos

def mutar(populacao):
    mutantes = []
    for ind in populacao:
        if random.random() < TAXA_MUTACAO:
            bin_ind = list(format(ind, f'0{NUM_BITS}b'))
            pos = random.randint(0, NUM_BITS - 1)
            bin_ind[pos] = '1' if bin_ind[pos] == '0' else '0'
            novo = int(''.join(bin_ind), 2)
            mutantes.append(min(novo, MAX_X))
        else:
            mutantes.append(ind)
    return mutantes

def elitismo(populacao_antiga, populacao_nova):
    melhor_antigo = max(populacao_antiga, key=avaliar)
    pior_novo_idx = min(range(len(populacao_nova)), key=lambda i: avaliar(populacao_nova[i]))
    populacao_nova[pior_novo_idx] = melhor_antigo
    return populacao_nova

def main():
    populacao = pop_inicial()
    geracao = 1

    print(f'\nGeração {geracao} inicial: {populacao}')
    
    while geracao < MAX_GERACOES:
        geracao += 1
        pais = [roleta(populacao) for _ in range(2)]
        filhos = crossover(*pais)
        filhos = mutar(filhos)
        filhos = elitismo(populacao, filhos)

        print(f'Geração {geracao}: {filhos} | Melhor: {max(filhos)}')

        if filhos.count(MAX_X) >= 3:
            print(f'\nCritério de parada atingido na {geracao}ª geração com 3 indivíduos = {MAX_X}')
            populacao = filhos
            break

        populacao = filhos

    print('\nResultados finais:')
    for ind in sorted(populacao, reverse=True):
        print(f'Indivíduo: {ind} -> f(x) = {avaliar(ind)}')
    print(f'\nMelhor valor encontrado: x = {max(populacao)} -> f(x) = {avaliar(max(populacao))}')

main()