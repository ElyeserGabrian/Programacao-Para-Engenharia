def ValorImc( altura, peso):
    imc = peso/(altura**2)
    return imc


def main():
    peso = float(input("Informe seu Peso: "))
    altura = float(input("Informe sua Altura: "))

    result = ValorImc(altura, peso)

    print(f"Seu Indice de Massa Corporal é igual a {result:.2f}")

    if result < 18.85:
        print("I é um graveto?")
    elif result >= 18.85 and result <= 24.9:
        print("Parabens, seu peso esta normal")
    elif result >= 25.0 and result <= 29.9:
        print("Ta engordando pae!")
    elif result >= 30:
        print("'SE VAI MORER'")



if __name__ =="__main__":
    main()