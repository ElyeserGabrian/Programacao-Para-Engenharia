# 3 – Elabore um script em linguagem Python que, dados dois inteiros x e y,
# retorna uma lista com todos os valores entre x e y (inclusive), considerando x <
# y. Exemplos x = 2, y = 6, resultado = [2, 3, 4, 5, 6]
lista = list()
x = int(input("digite o valor de X"))
y = int(input("digite o valor de Y"))
if x < y:
    for i in  range(x, y+1):
        lista.append(i)
elif x > y:
    for i in range(y, x+1):
        lista.append(i)

print(lista)