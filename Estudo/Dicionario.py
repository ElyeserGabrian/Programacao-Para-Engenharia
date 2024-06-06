# Criando um dicionário
dic = {'a': 1, 'b': 2, 'c': 3}

# Acessando e modificando valores
print(dic['a'])        # Saída: 1
dic['d'] = 4            # Adicionando um novo par chave-valor
print(dic.get('b'))     # Saída: 2
print(dic.get('x'))     # Saída: None
print(dic.setdefault('e', 5))  # Saída: 5 (adiciona 'e': 5)
print(dic)              # Saída: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Verificando e manipulando chaves e valores
print('b' in dic)       # Saída: True
print(dic.keys())       # Saída: dict_keys(['a', 'b', 'c', 'd', 'e'])
print(dic.values())     # Saída: dict_values([1, 2, 3, 4, 5])
print(dic.items())      # Saída: dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
