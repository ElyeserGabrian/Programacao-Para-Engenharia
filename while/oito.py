votos = 10
cand_1 = 0 
cand_2 = 0 
cand_3 = 0 
cand_4 = 0 
nulo = 0 
branco = 0
while votos != 0:
    votos = int(input("Digite o codigo do seu eleitor: "))
    if votos == 1:
        cand_1 += 1
    elif votos == 2:
        cand_2 += 1
    elif votos == 3:
        cand_3 += 1
    elif votos == 4:
        cand_4 += 1
    elif votos == 5:
        nulo += 1
    elif votos == 6:
        branco += 1
print(f"Candidato 1: {cand_1}\nCandidato 2: {cand_2}\nCandidato 3: {cand_3}\nCandidato 4: {cand_4}\nNulo: {nulo}\nBranco: {branco}")
