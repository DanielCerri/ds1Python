import os
os.system("cls")
#Estrutura de repetição for
#o numero colocado no range é a quantidade de vezes a ser repetido
#por boas praticas usa-se a variavel i no for, porem pode ser qualquer nome 

# #for com 1 parametro
# for i in range(10): #i começa em 0 vai até range-1 (0 a 9)
#     print("senai",i)

# #for com 2 parametros
# for i in range(20,30):#i começa em 20 e vai até range-1 (29) (20 a 29)
#     print(i)

# #for com 3 parametros
# for i in  range(0,10,5): # i começa em 0 vai até range -1 (9) e incrementa de 5 em 5 (0,5)
#     print(i)


#atividade1

# for silencio in range(1,50):
#     print(silencio)


# #atividade2 
# for silencio in range(-30,16):
#     print(silencio)

# #atividade tabuada

# n = int(input("digite um numero da tabuada: "))
# if n >0 and n<11:
#     for i in range(1,11):
#         print(n,"X",i,"=", n*i)
# else:
#     print("DEVE SER ENTRE 1 A 10")

#desafio maior numero


n=0
maiornumero=0
for i in range(5):
	n=int(input("Digite um numero: "))
	if i==0:
		maiornumero = n 
	if n > maiornumero :
		maiornumero = n

print(f"MAIOR NUMERO: {maiornumero}")