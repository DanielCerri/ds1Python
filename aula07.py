import os
os.system("cls")
#Estrutura de repetição for
#o numero colocado no range é a quantidade de vezes a ser repetido
#por boas praticas usa-se a variavel i no for, porem pode ser qualquer nome 

# #for com 1 parametro
for i in range(10): #i começa em 0 vai até range-1 (0 a 9)
    print("senai",i)
else:
    print("é executado quando o for termina")
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

# #desafio maior numero


# n=0
# maiornumero=0
# for i in range(5):
# 	n=int(input("Digite um numero: "))
# 	if i==0:
# 		maiornumero = n 
# 	if n > maiornumero :
# 		maiornumero = n

# print(f"MAIOR NUMERO: {maiornumero}")


#padaria

# print("PADARIA PAO MURCHO")


# precoPao= float(input("Digite o preço do pao: "))  

# print("PANIFICADORA PAO MURCHO")

# for i in range(1,51):
#     print(i,f" - R$:{round(precoPao*i,2)}")

# qtd = int(input("Digite a quantidade que gostaria de levar: "))
# total =  round(precoPao * qtd,2)
# print("TOTAL SEM DESCONTO: ",total)
# cupom = input("digite o cupom de desconto: ")

# if cupom =="paodeontem":
#     total = round(total - (total *0.10),2)
# else:
#     print("CUPOM INVÁLIDO!")


# print(f"TOTAL DA COMPRA: {total}")

# pagto = int(input("Digite a forma de pagto (APENAS O VALOR): NOTA2 | NOTA 5 | NOTA 10 | NOTA 50"))

# if pagto > total: 
#     print("TROCO DE R$: ", round(pagto - total,2))
# elif pagto < total: 
#     print(" DINHEIRO INSUFICIENTE , FALTAM R$: ", round(total-pagto,2))
# else:
#     print("NÃO TEM TROCO , PAGAMENTO OK!")


#max (parametros) -> retornar o maior valor





#votação
print("*"*30,"SIMULAÇÃO DE VOTAÇÃO","*"*30)

candidato1 = input("Digite seu nome: ")
candidato1Numero = input("Digite seu numero de candidatura: ")
candidato1Voto=0

candidato2 = input("Digite seu nome: ")
candidato2Numero = input("Digite seu numero de candidatura: ")
candidato2Voto=0

candidato3 = input("Digite seu nome: ")
candidato3Numero = input("Digite seu numero de candidatura: ")
candidato3Voto=0

print("-"*60)

print(f"""
	ELEIÇÃO CANDIDATOS:
	{candidato1} pressionar {candidato1Numero}
	{candidato2} pressionar {candidato2Numero}
	{candidato3} pressionar {candidato3Numero}
  """) 

for i in range(10):
	voto = input("Digite o numero do candidato para votar: ")
    
	if voto == candidato1Numero or voto == candidato2Numero or voto ==candidato3Numero:
		match voto: 
			case _ if voto == candidato1Numero:
				candidato1Voto =  candidato1Voto +1 
				print(f"VOTO COMPUTADO PARA {candidato1}")

			case _ if voto == candidato2Numero:
				candidato2Voto =  candidato2Voto +1 
				print(f"VOTO COMPUTADO PARA {candidato2}")

			case _ if voto == candidato3Numero:
				candidato3Voto =  candidato3Voto +1 
				print(f"VOTO COMPUTADO PARA {candidato3}")

	else:
		print("CANDIDATO NÃO ENCONTADO, VOTO ANULADO!")

print("RESULTADO DA ELEIÇÃO: ")
print(f""" 

	{candidato1} : {candidato1Voto} votos
	{candidato2} : {candidato2Voto} votos
	{candidato3} : {candidato3Voto} votos

""")

maiorVoto = max(candidato1Voto,candidato2Voto,candidato3Voto)

if maiorVoto == candidato1Voto and candidato1Voto != candidato2Voto and candidato1Voto != candidato3Voto:
	print(f"VENCEDOR {candidato1}")
elif maiorVoto == candidato2Voto and candidato2Voto != candidato1Voto and candidato2Voto != candidato3Voto:
	print(f"VENCEDOR {candidato2}")
elif maiorVoto == candidato3Voto and candidato3Voto != candidato1Voto and candidato3Voto != candidato2Voto:
	print(f"VENCEDOR {candidato3}")
else:
	print(" VOTAÇÃO EMPATADA , SERA NECESSARIO NOVO TURNO!")