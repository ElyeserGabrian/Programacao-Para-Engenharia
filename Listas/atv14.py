# 14 - Elabore um código que leia a temperatura média de cada mês do ano e
# guarde em uma lista. Com isso, efetue a média anual das temperaturas e
# mostre todas que estão acima da média anual e em que mês elas ocorreram
# (Ex.: 1 – Janeiro, 2 – Fevereiro, etc)
mes = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
tem = []
acima = {}
for k in mes:
    tem_mes = int(input(f"Digite a temperatura media do mes de {k} : "))
    tem.append(tem_mes)
    for i in range(len(mes)):
     i+=1
     media_anual = sum(tem)/i

for i in range(len(mes)):
    if tem[i] > media_anual:
        acima[mes[i]] = tem[i]

print("\nTemperaturas médias registradas:")
for i in range(len(mes)):
    print(f"{mes[i]}: {tem[i]}°C")

print(f"\nMédia anual das temperaturas: {media_anual:.2f}°C")

print("\nMeses com temperaturas acima da média anual:")
for month, temp in acima.items():
    print(f"{month}: {temp}°C")

        