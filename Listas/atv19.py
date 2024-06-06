# 19 – Leia um vetor com 20 número inteiros. Escreva os elementos do vetor
# eliminando elementos repetidos.

vetor = [1, 2, 3, 4, 5, 5, 6]
sem_rep = []
sem_rep.append(set(vetor))
print(sem_rep)