#Crie um programa com dois vetores de 10 posições e insira em outro 
#vetor, nas posições pares, os valores do primeiro e, nas posições 
#ímpares, os valores do segundo. 


vetor=[0,1,2,3,4,5,6,7,8,9]
vetor2=[9,8,7,6,5,4,3,2,1,0]

#vetor=[1,3,5,7,9]  prof.
#vetor2=[2,4,6,8,10]

vetorT= [0]*10

for i in range(10):
    if i % 2 == 0:
        indice= int (i/2)
        vetorT[i]=vetor[indice]
    else:
        indice = int(i/2)
        vetorT[i] = vetor2[i]
     
print(vetorT)
