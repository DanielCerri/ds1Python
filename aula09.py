import os
os.system("cls")
#funcoes
#ORGANIZAR O CODIGO E EVITAR DUPLICIDADE
#def nomeFuncao():
#A funcao so sera executada ao ser chamada pelo nome

#funcao sem parametro sem retorno
# def Conteudo():
#     print("explicando funcao")
#     print("vai cair na prova")

# Conteudo()

#funcao com parametro
# def ExemploParametro(n1,n2):
#     print(n1+n2)
#     print(n1*n2)

# ExemploParametro(50,75)

#funcao com retorno
# def Retorno():
#     ex =  "bom dia"
#     return ex

# teste = Retorno()

# print(teste)

#atividade1
# def boas_vindas():
#     print("Bem-vindo ao curso de Python!")

# boas_vindas()

#atividade2

# def saudacao(nome):
#     print(f"ola, {nome}")

# saudacao("daniel")


#atividade3

# def subtracao (num1,num2):
#     sub = num1-num2
#     return sub

# subt = subtracao(100,50)

# print("o valor subtraido é", subt)

#atividade4
# def ConverteGrau():
#     f = float(input("Digite o valor em grausº Fahrenheit: "))
#     calculo = ((f-32) / 9) * 5
#     print(f"VALOR EM GRAUS º CELSIUS É {calculo:.2f}")

# ConverteGrau()


#dolar real

# def Menu():
#     os.system("cls")
#     print("="*30,"MENU","="*30)
#     print(""" 
#     1-dolar para real
#     2- real para dolar
#     3-sair
#     """)

# def dolar_real():
#     valor = float(input("Digite quantos $Dolares gostaria de converter $: "))
#     print(f"VALOR EM REAIS: RS$: {valor*5.67:.2f}")

# def real_dolar():
#     valor = float(input("Digite quantos $Reais gostaria de converter R$: "))
#     print(f"VALOR EM Dolar: $: {valor/5.67:.2f}")

# opcao =0 

# Menu()
# while opcao !=3:
#     opcao = int(input("Digite a opção desejada: "))

#     if opcao ==1:
#         dolar_real()
#     elif opcao ==2:
#         real_dolar()
#     elif opcao ==3:
#         print("SAIU DO PROGRAMA")
#     else:
#         print("OPÇÃO INVÁLIDA!")



# def maior_valor(n1,n2,n3):
#     print(f"maior : {max(n1,n2,n3)}")

# a1=float(input("Digite um numero: "))
# a2=float(input("Digite um numero: "))
# a3=float(input("Digite um numero: "))


# maior_valor(a1,a2,a3)


# def conta_vogais(palavra):
#     contador=0
#     for l in palavra:
#         if l == "a"  or l =="e" or l =="i" or l =="o" or l =="u" or l in "âãàáèêéíìîúùûõòóô":
#             contador +=1
#     print(f"a palavra tem {contador} vogais")

# conta_vogais(input("Digite uma palavra: ").lower())