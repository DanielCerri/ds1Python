import os 
os.system("cls")
# #IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
# #ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# # ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
# #  SE MENOR QUE 12 -> CRIANÇA
# #  SE MENOR QUE 18 -> ADOLESCENTE
# #  SE MENOR QUE 60 -> ADULTO
# #  SE NAO -> IDOSO


# # NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")



#atividade 1
#replace("valor1","valor2")-> Substitui o valor 1 pelo valor2

# n1 = float(input("digite a 1º nota: ").replace(",","."))
# n2 = float(input("digite a 2º nota: ").replace(",","."))

# media = (n1+n2)/2
# #:.2f -> formata para 2 casas decimais apenas no fstring
# print(f"Média: {media:.2f}")

# if media <5:
#     print("REPROVADO")
# elif media >=5 and media<=7:
#     print("EM RECUPERAÇÃO")
# else:
#     print("APROVADO")


#atividade IMC
# peso = float(input("DIGITE SEU PESO: "))
# altura = float(input("Digite sua altura: "))

# imc = round( peso / (altura*altura), 2 ) 

# print(f"Seu imc: {imc}")

# if imc <17:
#     print("muito abaixo do peso")
# elif imc >=17 and  imc<= 18.49 :
#     print("abaixo do peso")
# elif imc >=18.5 and  imc<= 24.99 :
#     print("peso normal")
# elif imc >=25 and  imc<= 29.99 :
#     print("acima do peso")
# elif imc >=30 and  imc<= 34.99 :
#     print("ob 1")
# elif imc >=35 and  imc<= 39.99 :
#     print("ob 2")
# else:
#     print(" ob 3 mórbida ")


# raw string

print(r"""  

       //  ||\ \
 _____//___||_\ \___
 )  _          _    \
 |_/ \________/ \___|
___\_/________\_/______                      

""")


print("programa de reajuste autocar")

salario = float( input("Digite seu salario: ") )

percentual = 0 

if salario <= 2799.99 :
    percentual = 0.20
elif salario >= 2800 and salario<=6999.99 : 
    percentual = 0.15
elif salario >= 7000 and salario<=14999.99 : 
    percentual = 0.10
else:
    percentual= 0.05

print("-"*40)
print(f"SALARIO ANTERIOR AO REAJUSTE R$: {salario}")
print(f"Percentual aplicado: {percentual*100} %")
print(f"Valor do aumento:  {salario * percentual:.2f}")
print(f"Novo salario R$: {salario + (salario * percentual):.2f}")