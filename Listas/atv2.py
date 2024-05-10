# 2) Desenvolva um script em linguagem Python que peça as quatro notas de 10
# alunos, calcule e armazene num vetor a média de cada aluno, imprima o
# número de alunos com média maior ou igual a 7.
tent = 10
i = 0 
lista = list()
aluno = 0
while i < tent:
    i+=1
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    n4 = float(input("Digite a nota 4: "))
    print("********** next student ***********")
    media = (n1 + n2 + n3 + n4)/4
    lista.append(media)
for j in lista:
    if j >= 7:
        aluno+=1
print(f"{aluno} aluno tirou media maior igual a sete")
print(lista)
    

