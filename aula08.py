import os 
import random
os.system("cls")
#estrutura de repetição while (enquanto)
#enquanto uma condição for verdadeira ele executa o looping até que ela seja falsa

# aula = 8
# while aula==8:
#     print("silencio!")
#     aula=9
# else:
#     print("é executado quando o while é falso")

# while incremental
# i= 0 

# while i <10:
#     #i = i+1 #incrementar de 1 em 1
#     i+=1 #incremento simplificado mesma coisa que i = i+1
#     print("valor da variavel = ", i)
 


# EXPLICANDO NOVAMENTE.......

#WHILE É UMA ESTRUTURA DE REPETIÇÃO NA QUAL REPETE UM LOPING
#ENQUANTO ALGUMA CONDIÇÃO FOR VERDADEIRA
#POR SE TRATAR DE UMA CONDIÇÃO VOCE DEVE USAR OS OPERADORES CONDICIONAIS
#OPERADORES: < <= > >= == != 


# exemplo = 0

# while exemplo ==9 :
#     print("isso é um exemplo")
#     exemplo+=1


#atividade 1
#mostrar de 2 a 18

# x = 2

# while x <19:
#     print(x)
#     x+=1

#atividade 2

# x=0 

# while x >-51:
#     print(x)
#     x-=1
#     #x=x-1


#atividade While 

# print("""
# 1- cadastrar nome
# 2- cadastrar cpf
# 3- cadastrar idade
# 4- sair
#  """)

# opcao = 0 

# while opcao != 4 : 
#     opcao = int(input("Digite a opção desejada: ")) 

#     if opcao == 1:
#         nome = input("Digite seu nome: ")
#     elif opcao ==2 :
#         cpf = input("Digite seu cpf: ")
#     elif opcao == 3: 
#         idade = int(input("Digite sua idade :"))
#     elif opcao ==4: 
#         print("DADOS CADASTRADOS")
#         print(f"NOME : {nome}")
#         print(f"CPF : {cpf}")
#         print(f"IDADE : {idade}")
#     else:
#         print("opção invalida!")

#atividade 1

# senha = 0

# while senha != 9999: 
#     senha = int(input("Digite a senha (4 numeros): "))
#     if senha ==1505:
#         print("sennha correta")
#     else:
#         print("senha incorreta")
# else:
#     print("programa encerrado")

#atividade 2

# print("adivinhe o numero ")

# maquina = 0
# numeroUsuario = "" 

# while maquina != numeroUsuario :

#     maquina = random.randint(1,10)
#     numeroUsuario = int(input("Digite um numero: "))

#     if maquina == numeroUsuario:
#         print("PARABENS VOCE ACERTOU :)")
#         print(f"Voce digitou {numeroUsuario}")
#         print(f"A maquina pensou em {maquina}")
#     else:
#         print("VOCE ERROU :(")
#         print(f"Voce digitou {numeroUsuario}")
#         print(f"A maquina pensou em {maquina}")
# else:
#     print("programa encerrado! ")



#atividade banco 

# print("""
# 1-deposito
# 2-saque
# 3-mostra saldo
# 4-sair do programa
# """)

# opcao = 0 
# saldo=0

# while opcao != 4 : 
#     opcao = int(input("digite a opção desejada :"))

#     if opcao == 1:
#         dep = float(input("Digite o valor do Deposito: R$: "))
#         saldo = saldo + dep
#     elif opcao ==2:
#         saque = float(input("Digite o valor do saque: R$: "))
#         saldo = saldo - saque
#     elif opcao ==3:
#         print(f"SALDO DA CONTA R$: {saldo}")
#     else:
#         print("opção invalida")

# else:
#     print("programa encerrado")    



# print("  atividade guanabara 2 valores  ")

# print("""
#       1-somar
#       2-multiplicar
#       3-maior
#       4-novo numeros
#       5-sair do programa 
#       """)

# opcao = 0 

# n1 = float(input("Digite um numero: "))
# n2 = float(input("Digite um outro numero: "))

# while opcao !=5:
    
#     opcao = int(input("Digite a opção desejada: "))

#     if opcao == 1:
#         print(f"SOMA DOS NUMEROS: {n1+n2}")
#     elif opcao ==2 :
#         print(f"MULTIPLICAÇÃO DOS NUMEROS: {n1*n2}")
#     elif opcao == 3:
#         maiorNumero = max(n1,n2)
#         print(f"O MAIOR NUMERO É {maiorNumero}")
#     elif opcao ==4:
#         n1 = float(input("Digite um numero: "))
#         n2 = float(input("Digite um outro numero: "))    

# else:
#     print("programa encerrado")


#atividade notas


print("CALCULADORA DE NOTAS ")
print("CONVERSÃO DO VALOR EM NOTAS DE 100 , 50 , 20 , 10 , 5 E 1")
print("Digite um valor diferente de -1 para continuar fazendo a conversão ! ")

valor = 0

while valor != -1:

    valor = int(input("DIGITE O VALOR PARA CONVERTER: "))

    if valor > -1:
        if valor // 100 != 0: 
            print(f"{valor // 100} notas de 100")
            valor = valor - (valor // 100 * 100)
        
        if valor // 50 != 0: 
            print(f"{valor // 50} notas de 50")
            valor = valor - (valor // 50 * 50)
        
        if valor // 20 != 0: 
            print(f"{valor // 20} notas de 20")
            valor = valor - (valor // 20 * 20)
        
        if valor // 10 != 0: 
            print(f"{valor // 10} notas de 10")
            valor = valor - (valor // 10 * 10)

        if valor // 5 != 0: 
            print(f"{valor // 5} notas de 5")
            valor = valor - (valor // 5 * 5)

        if valor // 1 != 0: 
            print(f"{valor // 1} notas de 1")
            valor = valor - (valor // 1 * 1)

else:
    print("programa encerrado! ")