import os
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

print("""
1- cadastrar nome
2- cadastrar cpf
3- cadastrar idade
4- sair
 """)

opcao = 0 

while opcao != 4 : 
    opcao = int(input("Digite a opção desejada: ")) 

    if opcao == 1:
        nome = input("Digite seu nome: ")
    elif opcao ==2 :
        cpf = input("Digite seu cpf: ")
    elif opcao == 3: 
        idade = int(input("Digite sua idade :"))
    elif opcao ==4: 
        print("DADOS CADASTRADOS")
        print(f"NOME : {nome}")
        print(f"CPF : {cpf}")
        print(f"IDADE : {idade}")
    else:
        print("opção invalida!")