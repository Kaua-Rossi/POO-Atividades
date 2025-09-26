tipo = input("Digite o tipo de triângulo para saber coordenadas que formam esse tipo de triângulo (equilatero, isósceles, escaleno): ")

if tipo.lower() in ["equilátero", "equilatero"]:
    print("Sugestão de coordenadas para triângulo EQUILÁTERO: (0,0), (2,0), (1, 1.7320508075688772)")
elif tipo.lower() == "isósceles":
    print("Sugestão de coordenadas para triângulo ISÓSCELES: (0,0), (2,0), (1,1)")
elif tipo.lower() == "escaleno":
    print("Sugestão de coordenadas para triângulo ESCALENO: (0,0), (4,0), (0,3)")
else:
    print("Tipo de triângulo desconhecido.")
