frase = input("Digite uma frase ").lower()
if frase == frase[::-1]:
    print("É um palindromo")
else:
    print("Não é um palindromo")