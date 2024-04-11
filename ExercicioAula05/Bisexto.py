ano = int(input("Digite um ano: "))
for i in range(2000, ano+1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        i+1
        print(f"BiSexto! = {i}")
    else:
        print("Nao é bisexto ")

