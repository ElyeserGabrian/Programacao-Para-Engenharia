import math
pi = math.pi
R = float(input("Informe o raio do circulo maior: "))
r = float(input("Informe o raio do circulo menor: "))
A = pi * R**2
a = pi * r**2
AC = A - a
print(f"A área da Coroa do Circulo é igual: {AC}")