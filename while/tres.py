media = 0
negativo = 0
positivo = 0 
percentual1 = 0
percentual = 0  
for i in range(1,5):
    numero = int(input("Digite o numero: "))
    media += numero / 4
    if numero < 0:
        negativo += 1
        percentual = (negativo/4)*100
    else:
        positivo += 1
        percentual1 = (positivo/4)*100
print(f"Media{media}, Positivos {positivo}, Negativo {negativo}, Percentual Negativo {percentual}, Percentual Positivo {percentual1}")
