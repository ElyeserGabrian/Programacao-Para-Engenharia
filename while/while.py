tent = 999999999999999
i = 0
senha = "987654"
while i < tent:
    i+=1 
    new_senha = input("Digite uma senha ")
    if new_senha == senha:
        print("Cofre Aberto")
        break
    else:
        print("Valor incorreto ")
        