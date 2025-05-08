import os
os.system("cls")

#Continuação Input com Int e Float
#int() -> converte para inteiro
#float()-> converte para n quebrado e inteiro
#exemplo1
# numero = 10
# numero2 = input("digite um numero: ")
# print("o tipo de numero é,", type(numero2))
# soma = numero + int(numero2)
# print(f"soma de {numero} + {numero2}  = ", soma)

#exemplo2 
# num1 = input("digite um numero: ")
# soma = float(num1) + 15 
# print("A Soma de ",num1 , "+", "15" ,"=", soma)

#exemplo 3
# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero: "))

# soma = n1+n2

# print(f"a soma de {n1} + {n2} = ", soma)


#atividade 1


# n1 = float(input("digite um numero:  "))
# n2 = float(input("digite um outro  numero:  "))
# soma = n1*n2
# print(f"A multiplicação de {n1} * {n2} = {soma}")

# atividade 2

# numero = int(input("digite um numero:  "))

# print(f"Sucessor: {numero+1}")
# print(f"Antecessor: {numero-1}")

#atividade 3

# nasc = int(input("Digite o ano do seu nascimento: "))
# idade = 2025 - nasc 

# print(f"Sua idade é {idade} anos")

#porcentagem 
# print("25% de 100 = ", 0.25 * 100 )
# print("4% de 400 = ", 0.04 * 400)
# print("99% de 1525= ", 0.99 * 1525)

# #supondo que um produto custa 150 reais
# #e o caixa deu um desconto de 15% 
# exemplo = float(input("digite o preco do produto: "))
# desconto = 0.15 * exemplo
# print("o preco do produto com 15% de desconto é ", exemplo-desconto)

# Escreva um programa em python que leia 2 itens de um supermercado você deve armazenar
# o nome e o valor do item, no final aplique 10% de desconto no primeiro item 25% de desconto 
# no segundo item .
# Calcule o valor total da compra e mostre o nome e o valor com desconto de cada item.


#Atividade Porcentagem

print("*"*15,"SUPERMERCADO SENAI","*"*15)

prod1 = input("digite o nome do 1º produto: ")
valor1 = float(input("digite o valor desse produto: "))

prod2 = input("digite o nome do 2º produto: ")
valor2 = float(input("digite o valor desse produto: "))

desconto1 =   valor1*0.10
desconto2 =   valor2*0.25

valorfinal1 = round(valor1-desconto1,2)
valorfinal2 = round(valor2-desconto2,2)

print("."*20,"CAIXA","."*20)

print(f"{prod1} custa {valor1} com 10% = {valorfinal1}")
print(f"{prod2} custa {valor2} com 25% = {valorfinal2}")

print("."*20,"TOTAL","."*20)

total = valorfinal1+valorfinal2
print(f"TOTAL DA COMPRA -> R$: {total}" )

#round(valor,qtdCasasDecimais) -> faz o arredondamento dos valores







