# 2 – Elabore um script em linguagem Python, utilizando Dicionários, que
# contenha 4 funcionários, com o índice numérico e seu nome. Em seguida,
# solicite do usuário demitir um dos funcionários conforme o número de
# cadastro e mostre na tela os funcionários restantes.
func = {
    1: "Elyeser",
    2: "Gabriel",
    3: "Felipe",
    4: "André"
}
while True:
    resp = input("Voçê realmente deseja demitir um funcionario? S/N: ").upper()
    if resp == "N":
        break
    else:
        id = int(input("Digite o numero do cadastro do funcionario: "))
        if id in func:
            del func[id]
            for cod, nome in func.items():
                print("Funcionarios restantes")
                print(f"codigo {cod} Nome do func {nome}")
        else:
            print("Este numero de cadastro não existe! ")