n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
print(f"N1 = antes {n1}")
print(f"N2 = antes {n2}")
n1, n2 = n2, n1
print("\nValores depois da troca:")
print("N1 = ", n1)
print("N2 = ", n2)

