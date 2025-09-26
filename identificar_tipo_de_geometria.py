import math
from itertools import combinations

x1, y1 = map(float, input("Digite a primeira coordenada (x1 y1): ").split())
x2, y2 = map(float, input("Digite a segunda coordenada (x2 y2): ").split())
x3, y3 = map(float, input("Digite a terceira coordenada (x3 y3): ").split())
x4, y4 = map(float, input("Digite a quarta coordenada (x4 y4): ").split())

pontos = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

distancias = [math.dist(p1, p2) for p1, p2 in combinations(pontos, 2)]

distancias.sort()

lados = distancias[:4]
diagonais = distancias[4:]

lado_curto1 = lados[0]
lado_curto2 = lados[1]
lado_longo1 = lados[2]
lado_longo2 = lados[3]
diag1 = diagonais[0]
diag2 = diagonais[1]

if (math.isclose(lado_curto1, lado_curto2) and
    math.isclose(lado_longo1, lado_longo2) and
    math.isclose(diag1, diag2) and
    math.isclose(lado_curto1**2 + lado_longo1**2, diag1**2)):

    if math.isclose(lado_curto1, lado_longo1):
        print("As coordenadas formam um QUADRADO.")
    else:
        print("As coordenadas formam um RETÂNGULO.")
else:
    print("As coordenadas NÃO formam um quadrado ou retângulo.")