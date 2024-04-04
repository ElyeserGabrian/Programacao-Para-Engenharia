import math
def calcularvazao(diametro, fast):
    area = math.pi * (diametro / 2)**2
    vazao = area * fast
    return vazao


def main():
    diametro = float(input("Informe o diametro interno do tubo: "))
    fast = float(input("Informe a velocidade do fluido: "))

    resultado = calcularvazao(diametro, fast)

    print(f"A vazão do fluido no tubo é de {resultado:.2f} metros cúbicos por segundo.")

if __name__ == "__main__":
    main()
