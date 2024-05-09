x = int(input("digite o primeiro num: "))
y = int(input("digite o segundo num: "))
soma = 0
for i in range(x+1, y):
        print(i, end=" ")
        soma += i
print("Soma: ",soma)
