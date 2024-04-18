# 19) Crie um script em linguagem Python que leia três números e mostre o maior e o menor deles.
n1 = int(input("N1= "))
n2 = int(input("N2= "))
n3 = int(input("N3= "))
menor = min(n1, n2, n3)
print(f"O menor Numero entre {n1}, {n2} e {n3} é {menor}")
