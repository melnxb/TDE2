#Faça um programa que leia um vetor de 10 posições e verifique se 
#existem valores iguais e os escreva na tela. 

from enum import unique
from multiprocessing.reduction import duplicate
from typing import Counter

vetor1=[]
print('Digite 10 números:')
for i in range(10) :
    vetor1.append(input('Numero '+ str(i+1) + ':')) #já vai direto pro vetor
igual = {x for x in vetor1 if vetor1.count(x) > 1}
print(igual)

#rep = unique_everseen(duplicates(vetor1))
#print("Números repetidos: ")
