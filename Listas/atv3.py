# 3) Crie um script em linguagem Python que leia dois vetores com 5 elementos
# cada. Gere um terceiro vetor de 10 elementos, cujos valores deverão ser
# compostos pelos elementos intercalados dos dois outros vetores. Exibir na
# tela todos os vetores em linhas separadas.
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
c = []
for i, j in zip(a, b):
    c.append(i)
    c.append(j)
print(c)
