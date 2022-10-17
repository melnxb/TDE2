import random
num = [random.randint(0, 20) for x in range(50)]
print(num)

soma=num[0]+num[1]+num[2]+num[3]+num[4]+num[5]+num[6]+num[7]+num[8]+num[9]
soma2=num[10]+num[11]+num[12]+num[13]+num[14]+num[15]+num[16]+num[17]+num[18]+num[19]+num[20]
soma3=num[21]+num[22]+num[23]+num[24]+num[25]+num[26]+num[27]+num[28]+num[29]+num[30]
soma4=num[31]+num[32]+num[33]+num[34]+num[35]+num[36]+num[37]+num[38]+num[39]+num[40]
soma5=num[41]+num[42]+num[43]+num[44]+num[45]+num[46]+num[47]+num[48]+num[49]
somat= soma+soma2+soma3+soma4+soma5
print(somat)
#tentei de todo jeito fazer a soma sem chegar nessa situação tragica, mas não tava indo :'(

print(num.count(9))

#maior= max(num)
maior=0
menor=0
for i in num:
    if i ==0:
        maior=menor=num[i]
    else:
     if num[i]> maior:
        maior = num[i]
     if num[i]< menor:
        menor = num[i]
print('Maior número e menor número: ')
print(maior)
print(menor)