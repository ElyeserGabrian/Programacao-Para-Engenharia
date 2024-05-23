# 13 - Desenvolver um programa que leia a altura de 15 pessoas. Este programa
# deverá calcular e mostrar:
# a. A menor altura do grupo;
# b. A maior altura do grupo;
# c. Em uma lista cada um dos dados de entrada.
person = 3
list_heigth = []
i = 0 
while i < person:
    i+=1
    heigth = float(input(f"Digite a altura da {i}ª pessoa: "))
    list_heigth.append(heigth)
    max_heigth = max(list_heigth)
    min_heigth = min(list_heigth)
print(f"A maior altura do grupo é: {max_heigth} ")
print(f"A menor altura do grupo é: {min_heigth}")
print(f"Lista dos dados de entrada: {list_heigth}")