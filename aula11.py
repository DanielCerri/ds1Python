import os 
os.system("cls")

# dicionario = ["dia":"03/06/2025",2:2.5,"booleano":True]

# #inserir ou alterar valor no dicionario 
# dicionario["aluno"] = "kauaACORDE"

# #inserir ou alterar valor atraves do update()
# dicionario.update(["aluno2":"kauaSONINHO"])

# #recuperar valores em um dicionario
# valores = dicionario["aluno"]
# valores = dicionario.get(2)

# #excluir valores do dicionario 
# #dicionario.pop("aluno2") #-> excluir chave e valor atraves da chave

# #excluir todos valores
# #dicionario.clear()

# #print(valores)
# print(dicionario)

# #percorrendo dicionario por chave e valor
# for key, value in dicionario.items():
#     print(key, value)

# #percorrendo dicionario para capturar valores
# for values in dicionario.values():
#     print(values)

# #percorrendo dicionario para capturar chaves:
# for keys in dicionario.keys():
#     print(keys)

#atividade 1 

# carros = []
# carros["siennaBRANCO"]= 45000
# carros["porsche"] = 3000000 
# carros["kwid"] = 60000
# carros["onix"] = 90000
# carros["hrv"] = 156000

# for key,value in carros.items():
#     print( "MODELO: ", key , "-> ", "PREÇO R$: ", f"[value:.2f]" )

# #atividade 2
# futebol=[]

# for i in range(1,6):
#     time = input(f"Digite [i] º time: " )
#     serie=input("Digite a Serie: ")
#     futebol.update ([time : serie  ]) 
# else:
#     for key, value in futebol.items():
#         print(f"TIME: -> [key] -> Serie: [value]")


#atividade 3 

# dicionario = {}

# dicionario ["nome"] = "kaua"
# dicionario ["idade"] = 14
# dicionario ["telefone"] = "199999999"
# dicionario ["endereço"]="rua x nº y av z"

# print(dicionario["nome"])



#ex4


d = {}

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")

d.update({"nome": nome, "idade": idade, "telefone":telefone, "end": endereco } )

print(d)









