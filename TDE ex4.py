vetor = []

print ('Digite 5 numeros')
for i in range(5):
     vetor.append(input('Numero '+ str(i+1) + ': '))
vetor.reverse()
print(vetor)
