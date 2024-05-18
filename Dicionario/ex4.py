# 4 – Em um script Python com duas listas de três elementos com números
# inteiros, crie uma nova lista onde cada elemento é a soma dos elementos de
# mesma posição nas duas primeiras listas.
# Exemplo: Lista1 = [1, 4, 6] Lista2 = [2, 4, 3] Lista_resultante = [3, 8, 9]
Lista1 = [1, 4, 6]
Lista2 = [2, 4, 3]
lista_result = []
for i in range(len(Lista1)):
    lista_result.append(Lista1[i] + Lista2[i])
print(lista_result)

