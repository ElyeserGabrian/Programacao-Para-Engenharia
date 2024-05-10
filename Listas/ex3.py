# Em um script Python, crie uma lista vazia, que seja preenchida com
# notas de 3 alunos. Após a leitura das notas, mostrar a nota mais alta, a
# nota mais baixa, a média geral de notas, além de ordenar a lista de
# forma crescente.
lista = list()
for i in range(3):
    i+=1
    nota = float(input(f"Digite a nota do {i}º: "))
    lista.append(nota)
    maior = max(lista)
    menor = min(lista)
    media = sum(lista)/3
print(f"A maior nota digitado é {maior}")
print(f"A menor nota digitado é {menor}")
print(f"A media das notas digitado é {media}")

