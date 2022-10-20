vetor=[4,2,3,0,7,9,2,0,1,5,0,5,0,1,0]

for i in range (15):
    if vetor[i] == 0:
        anter = vetor[:i]
        prox = vetor[i+1: len(vetor)]
        vetor= anter + prox + [0] #poderia representar por -1; não precisaria se fosse lista;
print(vetor)