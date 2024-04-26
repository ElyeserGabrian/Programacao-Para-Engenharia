# 2) Para construir o programa a seguir, considere que os usuários só informarão
# números inteiros positivos. Crie um programa que receba 5 números digitados e, ao
# final, exiba a quantidade de números pares.
cont= 0
for i in range(1, 5+1):
    num = int(input("Digite um numero inteiro: "))
    if num % 2 == 0:
     cont+= 1 
print(f"A quantidade de numeros pares digitado foi igual a {cont}") 