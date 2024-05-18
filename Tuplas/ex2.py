p1 = (7.0, 8.3, 10.0, 6.5, 9.3)
p2 = (8.5, 6.9, 5.0, 7.5, 9.8)

media1 = sum(p1) / len(p1)
media2= sum(p2) / len(p2)

print(f"Média da turma na prova 1: {media1}")
print(f"Média da turma na prova 2: {media2:.2f}")
if media1 > media2:
    print(f"A turma obteve a melhor média na prova 1.")
else:
    print("A turma obteve a melhor média na prova 2.")