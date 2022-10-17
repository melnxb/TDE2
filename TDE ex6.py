from random import random

#vetor = [random.randint(0, 20) for x in range (20)]
#print(vetor)
vetor=[2,2,4,6,7,8,8,9,14,35,89,0,3,11,4,35,11,20,0,96]
print(vetor)
rep = {x for x in vetor if vetor.count(x) > 1}
print(rep)