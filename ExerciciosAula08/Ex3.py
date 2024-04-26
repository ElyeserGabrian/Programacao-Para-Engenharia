# 1) Elabore um programa que leia um número inteiro e indique se o número é primo
# ou não. Lembrando que os números primos são divisíveis somente por 1 e por ele
# mesmo. No entanto, o número 1 não é primo.
num = int(input("Digite um valor inteiro"))
if num > 1:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
else:
    print("O número precisa ser maior que 1 para ser primo.")
