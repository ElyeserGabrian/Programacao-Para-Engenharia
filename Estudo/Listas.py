# Criando uma lista vazia
lista = []

# Adicionando elementos
lista.append(10)
lista.append(20)
lista.append(30)
print(lista)  # Saída: [10, 20, 30]

# Removendo elementos
lista.remove(20)
print(lista)  # Saída: [10, 30]

# Inserindo um elemento em uma posição específica
lista.insert(1, 25)
print(lista)  # Saída: [10, 25, 30]

# Removendo e obtendo o último elemento
elemento = lista.pop()
print(elemento)  # Saída: 30
print(lista)     # Saída: [10, 25]

# Ordenando a lista
lista = [3, 1, 4, 2, 5]
lista.sort()
print(lista)  # Saída: [1, 2, 3, 4, 5]

# Revertendo a lista
lista.reverse()
print(lista)  # Saída: [5, 4, 3, 2, 1]

# Verificando a existência de um elemento
if 3 in lista:
    print("3 está na lista")
else:
    print("3 não está na lista")

# Obtendo o índice de um elemento
indice = lista.index(4)
print(f"O índice de 4 é: {indice}")

# Contando o número de ocorrências de um elemento
ocorrencias = lista.count(3)
print(f"O número de vezes que 3 aparece é: {ocorrencias}")

# Copiando a lista
copia_lista = lista.copy()
print(copia_lista)  # Saída: [5, 4, 3, 2, 1]

# Limpando a lista
lista.clear()
print(lista)  # Saída: []

# Criando uma lista desordenada
numeros = [5, 2, 9, 1, 5, 6]

# Ordenando a lista e salvando o resultado em uma nova lista
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)  # Saída: [1, 2, 5, 5, 6, 9]
