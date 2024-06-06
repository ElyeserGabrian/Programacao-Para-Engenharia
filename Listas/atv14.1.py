# 14 - Desenvolver um script em linguagem Python que leia nome, altura e peso
# de 15 pessoas. Este programa deverá armazená-los em um Dicionário, bem
# como calcular e mostrar:
# a. A menor altura do grupo;
# b. O peso médio do grupo;
# c. Uma lista dos nomes das pessoas em ordem alfabética.

dic = {
    "Nomes": [],
    "Alturas": [],
    "Pesos": []
}
cont = 2
i=0
while i < cont:
    i+=1
    nome = input(f"Digite o {i}º nome: ")
    alt = float(input(f"Digite a {i}º altura: "))
    peso = float(input(f"Digite o {i}º peso: "))

    dic["Nomes"].append(nome)
    dic["Alturas"].append(alt)
    dic["Pesos"].append(peso)
    for j in dic["Alturas"]:
        menor = min(dic["Alturas"])

    peso_media  = sum(dic["Pesos"])/ len(dic["Pesos"])

    ordenado = sorted(dic["Nomes"])

print(ordenado)
print(menor)
print(peso_media)

    

    

