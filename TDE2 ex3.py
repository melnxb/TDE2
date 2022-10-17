
from ast import Num

vetor=[]

while True:
    num = int(input("Digite um números inteiro e positivo: "))
    if num < 0:
        print("Número inválido!")
        break 
    else:
        vetor.append(num)
print(vetor)

maior5=0
numsPar=0
numsImpar=0
#numTotal

for i in vetor:
    if i > 5:
        maior5=+1
    if i%2 == 0:
        numsPar=+1
    if i%2 != 0:
        numsImpar=+1

print('Quantidade de números maiores que 5: ' + str(maior5))
print('Quantidade de números pares: ' + str(numsPar))
print('Quantidade de números impares: ' + str(numsImpar))

    



