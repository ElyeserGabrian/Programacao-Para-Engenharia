# 1 – Desenvolva um código em Python que adicione em um dicionário “d” os
# seguintes campos: nome, idade, endereço e telefone e mostre os dados no
# final.

d = {}
i = 0 
tent = 9999999999
while i < tent:
    i+=1
    nome = input("Digite o nome: ")
    age = int(input("Digite a idade: "))
    end = input("Digite o endereço: ")
    fone = int(input("Digite o telefone: "))
    dados = []
    dados.append(nome)
    dados.append(age)
    dados.append(end)
    dados.append(fone)
    d.update({i: dados})
    resp = input("Deseja continuar adicionando dados no dicionario s/n: ").lower()
    if resp == "n":
        break
print(d)
