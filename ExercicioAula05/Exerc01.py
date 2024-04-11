litros = float(input("Litros: "))
combust = input("Combustivel G - Gasolina ou A - Alcool: ").upper()

if combust == "G":
    valorlitro = 5.57
    if litros <=20:
        desc = 4/100
        valor = litros * valorlitro
        novo = valor * desc
        valornovo = valor - novo
        print(valornovo)
    elif litros > 20:
            desc = 6/100
            valor = litros * valorlitro
            novo = valor * desc
            valornovo = valor - novo
            print(valornovo)
if combust == "A":
    valorlitro = 4.98
    if litros <=20:
        desc = 2/100
        valor = litros * valorlitro
        novo = valor * desc
        valornovo = valor - novo
        print(valornovo)
    elif litros > 20:
            desc = 5/100
            valor = litros * valorlitro
            novo = valor * desc
            valornovo = valor - novo
            print(valornovo)

            