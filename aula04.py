import os
os.system("cls")
#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)



#atividade1

# idade = int(input("Qual a sua idade: "))

# if idade >= 18:
#     print("maior de idade")
# else:
#     print("menor de idade")


#atividade 2
#dica -> abrir if dentro do else

# idade = int(input("Qual a sua idade: "))

# if idade<0 or idade>120:
#     print("IDADE INVÁLIDA")
# else:
#     if idade >= 18:
#         print("maior de idade")
#     else:
#         print("menor de idade")

# #atividade 3

# email = input("digite o seu email: ")
# senha = input("digite a sua senha: ")

# if email == "python@senai.com"  and senha=="12345678":
#     print("AUTENTICADO")
# else:
#     os.system("color 4")
#     print("USUARIO OU SENHA INVÁLIDA! ")



#atividade maça

# qtd = int(input("Digite a qtd de maças que deseja levar: "))

# if qtd < 12 :
#     calc = qtd * 0.30
#     print("Voce ira pagar (0,30 uni) : R$:  " , calc)
# else :
#     calc = qtd * 0.25
#     print("Voce ira pagar (0,25 uni) : R$:  " , calc)

#atividade vogal consoante

# l = input("Digite um letra: ")

# if l =="a" or l =="e" or l =="i " or  l=="u" or l =="o" or l == "A" or l=="E" or l =="I" or l=="O" or l=="U": 
#     print("É VOGAL!")
# else :
#     print("É CONSOANTE!")

#reescrevendo de outra maneira
#upper() -> CONVERTER TUDO PARA MAIUSCULO
#lower() -> CONVERTER TUDO PARA MINUSCULO

# l = input("Digite um letra: ").lower()

# if l =="a" or l =="e" or l =="i " or  l=="u" or l =="o":
#     print("É VOGAL!")
# else :
#     print("É CONSOANTE!")

#reescrevendo de outra maneira
# AND(E) OR(OU) in(DENTRO -> apenas para string)

l = input("Digite um letra: ")

if l in "aeiouAEIOU":
    print("vogal")
else:
    print("consoante")





