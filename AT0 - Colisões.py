# recebe as coordenadas do primeiro retângulo e transforma os valores em números inteiros
xa0, ya0, xa1, ya1 = map(int, input().split())

# recebe as coordenadas do segundo retângulo
xb0, yb0, xb1, yb1 = map(int, input().split())

# verifica se os retângulos não se tocam comparando a posição do segundo vértice do primeiro retângulo com o primeiro vértice do segundo
if xa1 <= xb0 or xb1 <= xa0 or ya1 <= yb0 or yb1 <= ya0:
    print(0)  # não colidem
else:
    print(1)  # colidem
