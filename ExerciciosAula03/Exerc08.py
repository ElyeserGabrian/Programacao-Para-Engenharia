preco = float(input("Informe o preco original do Produto: "))
desc = float(input("Qual o valor do desc: "))
if desc == 10:
    d10 = preco * 0.1
    new_pre = preco - d10
    print(f"Preço Original: {preco}")
    print(f"valor do Desconto R$:{d10} Reais")
    print(f"Novo preço do Produto com 10% DE desconto (o GERENTE ficou doido): R$: {new_pre}")
elif desc == 20:
    d20 = preco * 0.2
    new_pre = preco - d20
    print(f"Preço Original: {preco}")
    print(f"valor do Desconto R$:{d20} Reais")
    print(f"Novo preço do Produto com 20% DE desconto (o GERENTE ficou doido): R$: {new_pre}")
elif desc == 30:
    d30 = preco * 0.3
    new_pre = preco - d30
    print(f"Preço Original: {preco}")
    print(f"valor do Desconto R$:{d30} Reais")
    print(f"Novo preço do Produto com 30% DE desconto (o GERENTE ficou doido): R$: {new_pre}")
else:
    print("DESCONTO INVÁLIDO!!!")





