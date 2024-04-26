# 3) Faça um programa que apresente um menu de opções para o cálculo das
# seguintes operações entre dois números:
# • adição (opção 1)
# • subtração (opção 2)
# • multiplicação (opção 3)
# • divisão (opção 4)
# • saída (opção 5)
# O programa deve possibilitar ao usuário a escolha da operação desejada, a
# exibição do resultado e a volta ao menu de opções. O programa somente termina
# quando for escolhida a opção de saída (opção 5).
opcao = 0
while opcao != 5:
    opcao = int(input("Digite: \nadição (opção 1) \nsubtração (opção 2) \nmultiplicação (opção 3) \ndivisão (opção 4) \nsaída (opção 5): \n"))
    match opcao:
        case 1:
            n1 = float(input("Digite um numero: "))
            n2 = float(input("Digite um numero: "))
            soma = n1 + n2
            print(soma)
        case 2:
            n1 = float(input("Digite um numero: "))
            n2 = float(input("Digite um numero: "))
            sub = n1 - n2
            print(sub)
        case 3:
            n1 = float(input("Digite um numero: "))
            n2 = float(input("Digite um numero: "))
            mul = n1 * n2
            print(mul)
        case 4:
            n1 = float(input("Digite um numero: "))
            n2 = float(input("Digite um numero: "))
            div = n1 / n2
            print(div)
