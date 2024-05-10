# Desenvolva um script em linguagem Python com uma lista vazia. Em
# seguida, leia e insira 5 valores inteiros na lista. Ao final mostre na tela, os
# valores contidos na lista. Ordem de entrada e inversa.
tent = 5 
i = 0 
lista_num = []
while i < tent:
    i+=1
    num = int(input(f"Digite {i}º numero inteiro: "))
    lista_num.append(num)
for j in lista_num:
    ordem = j
    print(ordem)
print("\n")
for k in reversed(lista_num):
    inversa = k
    print(inversa)    



