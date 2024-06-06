# Criando uma tupla
tupla = (1, 2, 3, 4, 5)

# Acessando elementos
print(tupla[0])     # Saída: 1
print(tupla[2])     # Saída: 3

# Verificando a existência de elementos
print(3 in tupla)   # Saída: True
print(6 not in tupla)   # Saída: True

# Desempacotamento de tuplas
a, b, c, d, e = tupla
print(a, b, c, d, e)   # Saída: 1 2 3 4 5

# Concatenação de tuplas
outra_tupla = (6, 7, 8)
tupla_concatenada = tupla + outra_tupla
print(tupla_concatenada)   # Saída: (1, 2, 3, 4, 5, 6, 7, 8)
