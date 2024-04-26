# 1) Desenvolva um gerador de tabuada, capaz de gerar a tabuada
# de qualquer número inteiro entre 1 à 10. O usuário deve informar
# de qual número ele deseja ver a tabuada.
valor = int(input("Digite um numero para saber a sua tabuada de 1 até 10: "))
for i in range(1, 11):
    produto = valor * i
    print(f"{i} x {valor} = {produto}")