import math

def AreaTriangulo(raio):
    area = math.sqrt(3)/4 * raio**2
    hexagono = area * 6

    return hexagono


def main():
    raio = float(input("Informe o raio do Hexagono Regular: "))

    hexa = AreaTriangulo(raio)

    print(f"A área de um hexagono Regular é de: {hexa:.2f}")

if __name__ == "__main__":
    main()