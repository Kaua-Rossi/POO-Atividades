import math

x1, y1 = map(float, input("Digite a primeira coordenada (x1 y1): ").split())
x2, y2 = map(float, input("Digite a segunda coordenada (x2 y2): ").split())
x3, y3 = map(float, input("Digite a terceira coordenada (x3 y3): ").split())

d1 = math.dist((x1, y1), (x2, y2))
d2 = math.dist((x2, y2), (x3, y3))
d3 = math.dist((x1, y1), (x3, y3))

if d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1:
    if math.isclose(d1, d2) and math.isclose(d2, d3):
        tipo = "equilátero"
    elif math.isclose(d1, d2) or math.isclose(d2, d3) or math.isclose(d1, d3):
        tipo = "isósceles"
    else:
        tipo = "escaleno"
    print(f"As coordenadas formam um triângulo {tipo}.")
else:
    print("As coordenadas não formam um triângulo.")