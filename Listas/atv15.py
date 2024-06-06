# 15 - Elabore um script que crie um dicionário na qual cada chave seja um
# caractere e seu valor seja o número de vezes que o caractere aparece na frase.
# Exemplo:
# "Digite uma frase para contar as letras:“ – eu sei
# Resposta {'e': 2, 'u': 1,
# ' ': 1, 's': 1, 'i': 1}
frase = "eu sei"
dic = {}
soma=0
for letra in frase:
    if letra in dic:
        dic[letra]+=1
    else:
        dic[letra] = 1
print(dic)
