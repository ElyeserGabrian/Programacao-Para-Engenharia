# 1) Desenvolva um script Python que lê vários números positivos via teclado. Quando o
# número lido for -1, o script deve parar e exibir a soma de todos os números positivos
# inseridos, a média desses números, o menor e o maior número digitado.
num = 0
quantidade = 0 
soma = 0
maior = 0
menor = 99999999999999999999
while num != -1:
      num = int(input("Digite um numero positivo "))
      if num > 0:       
        quantidade +=1
        soma += num
        media = soma / quantidade
        if num > maior:
            maior = num
        if num < menor:
            menor = num


print(f"soma {soma}")
print(f"media {media}")
print(f"menor {menor}")
print(f"maior {maior}")

