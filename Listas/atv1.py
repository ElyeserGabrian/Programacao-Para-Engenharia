# 1) Elabore um script em linguagem Python que leia de 10 números reais,
# inserindo-os numa lista e ao final, mostre-os na ordem inversa.
lista = []
for i in range(4):
    i+= 1
    num = float(input(f"Digite {i}º numero real: "))
    lista.append(num)
for j in reversed(lista):
    print(j)
