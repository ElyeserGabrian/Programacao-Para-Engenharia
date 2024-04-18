ld1 = input("Informe o primeiro lado do triângulo: ")
ld2 = input("Informe o segundo lado do triângulo: ")
ld3 = input("Informe o terceiro lado do triângulo: ")
triangulo = bool(False)
if ((ld1 + ld2) > ld3) or ((ld1 + ld3) > ld2) or ((ld2 + ld3) > ld1) or ((ld1 + ld2) > ld3):
    triangulo = True
    print(triangulo) 
    if triangulo == True:
        if ld1 == ld2 == ld3:
            tE = "Triângulo Equilátero: três lados iguais"
            print(f"{tE}")
        elif ld1 == ld2 or ld2 == ld3 or ld3 == ld1:
            tI = "Triângulo Isósceles: quaisquer dois lados iguais."
            print(f"{tI}")
        elif ld1 != ld2 != ld3:
            tES = "Triângulo Escaleno: três lados diferentes."
            print(f"{tES}")