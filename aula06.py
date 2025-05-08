import os,random
os.system("cls")

# #ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
# # SWITCH CASE ->  (match case) escolha caso ( a partir da versão 3.10)
# #match  valor:
# #   case valor:


# linguagem = 100

# match linguagem: 

#     case "python":
#         print(" é facil")
#     case "java":
#         print(" muito codigo , python faz com linhas menores")
#     case "c#":
#         print(" massa")
#     case "js":
#         print("sou do back")
#     case "html":
#         print("kauan nao dorme")
#     case 10:
#         print("entrou aqui !")
#     case _ :
#         print("outro caso")


#atividade dias da semana

# print("""
# 1-segunda
# 2-terça
# 3-quarta
# 4-quinta
# 5-sexta
# 6-sabado
# 7-domingo
# """)

# dia = float(input("digite um numero de 1 a 7: "))

# match dia:

#     case 1:
#         print("segunda")
#     case 2:
#         print("terça")
#     case 3:
#         print("quarta")
#     case 4:
#         print("quinta")
#     case 5:
#         print("sexta")
#     case 6:
#         print("sabado")
#     case 7:
#         print("domingo")
#     case _:
#         print("digitou errado!")




# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valortotal:.2f}")

#match case com if
# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")
  

#pedra papel tesoura
print("JOGO PEDRA PAPEL TESOURA")

papel = """
PAPEL
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
PEDRA
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
TESOURA
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

jogador = input("Escolha entre pedra, papel ou tesoura: ")
match jogador:
    case "pedra":
        jogador=pedra
    case "tesoura": 
        jogador =tesoura
    case "papel":
        jogador = papel

#1-> pedra , 2-> papel , 3->tesoura

maquina = random.randint(1,3)

match maquina:
    case 1:
        maquina=pedra
    case 2: 
        maquina =papel
    case 3:
        maquina =tesoura


print(f"voce escolheu  {jogador}")
print(f"maquina escolheu {maquina}")

match jogador:
    case _ if jogador == maquina:
        print("empate")
    case _ if jogador==pedra and maquina ==tesoura:
        print("Voce ganhou")
    case _ if jogador == tesoura and maquina ==papel:
        print("Voce ganhou")
    case _ if jogador == papel and maquina ==pedra:
        print("voce ganhou")
    case _ :
        print("voce perdeu")



