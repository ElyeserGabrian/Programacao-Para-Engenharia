# 5 – Desenvolva um script em linguagem Python, utilizando Dicionários, que
# solicite ao usuário inserir o nome de três produtos de mercado e seus
# respectivos preços e os mostre na tela.
produtos = {}
for i in range(3):
    i+=1
    nome = input(f"Digite o nome do {i}º produto: ")
    preco = float(input(f"Digite o preço do {i}º produto "))
    produtos.update({nome: preco})
for name, price in produtos.items():
    print(" ")
    print(f"Nome do Produto: {name}\nPreço do Produto: R${price}")
