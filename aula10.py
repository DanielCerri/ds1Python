import os,random 
os.system("cls")
# #listas -> realiza armazenamento de mais de 1 tipo de dado
# #conseguimos armazenar string, int , float, booleano na mesma variavel.... 
# #cada elemento possui um indice, que sempre começa em 0 por padrao

# #lista = [50,30,"daniel"] 

# lista=[]
# #adicionando elemento na lista
# lista.append("aula de listas")#0
# lista.append(100)#1
# lista.append("silencio")#2
# lista.append(5)#3
# lista.append("livia")#4
# lista.append(True)#5
# lista.append(99.99)#6

# print(lista)
# # x= input("digite alguma coisa..: ")

# # lista.append(x) #0
# # lista.append(input("digite alguma coisa..: ")) #1

# #remover elemento da lista
# #remove pela posição 
# #lista.pop(indice)
# #lista.pop(4)

# #remover pelo valor
# #lista.remove(valor)
# x=lista.pop(2)
# print(x)

# #limpar a lista inteira
# #lista.clear()

# #alterar um elemento na lista 
# lista[4]= "mariah"

# #percorrer a lista e exibir os valores -> lista[indice]
# print(f"tamanho lista {len(lista)}")

# for i in range(len(lista)):
#     print(lista[i])


#atividade lista

# produto = []

# opcao = 0 

# while opcao!= 4:

#     opcao = int(input("Digite a opção desejada: "))

#     if opcao == 1:
#         produto.append(input("Digite um produto: "))
#         print("PRODUTO ADICIONADO!")
#     elif opcao==2:
#         prod = input("Digite um produto para remover: ")
#         produto.remove(prod)
#         print("produto removido!")
#     elif opcao ==3:
#         produto.clear()
#         print("LISTA VAZIA!")
#     elif opcao ==5:
#         for i in range(len(produto)):
#             print(f"produto {i} ->  {produto[i]}")


#atividade soma lista
#primeiro exemplo
# lista=[]
# soma=0

# for i in range(10):
#     lista.append( float(input("Digite um numero: ")))
# else:
#     for i in range( len(lista) ):
#         soma = soma + lista[i] 
#     else:
#         print(soma)

# #segundo exemplo
# lista2=[]
# for i in range(10):
#     lista2.append( float(input("Digite um numero: ")))
# else:
#     print(sum(lista2)) #sum()-> realiza a soma de todos os valores


#atividade salto


# nome =  input("digite seu nome: ")

# lista = [] 

# while nome!="":

#     for i in range(1,6):
#         lista.append(float(input(f"Digite a distancia do {i}º salto: ")) ) 
#     else:

#         for i in range(len(lista)):
#             print(f" {i+1} º salto: {lista[i]}")

#         print(f"MEDIA DOS SALTOS DE {nome}: " , round(sum(lista)/len(lista),2))
#         nome =  input("digite seu nome: ")
#         lista.clear()
# else:
#     print("saiu do programa")



#metodo list() -> converte para lista

# palavra = list(input("digite uma palavra: "))

# acerto= ["_"]*len(palavra)
# print(acerto)

# letra = input("Digite uma letra: ")

# for i in range(len(palavra)): #i de 0 ate 6
#     if letra == palavra[i]:
#         acerto[i]=letra
# else:
#     print(acerto)  
     

#atividade zero
#julia
# nums = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1] 

# for i in range(len(nums)):

#     nums.remove(0)
#     nums.append(0)
#     print(nums)

# print(nums)


#resolvendo usando count
# contar = nums.count(0)

# for i in range(contar):
#     nums.remove(0)
# else:
#     for i in range(contar):
#         nums.append(0)

# print(nums)
#atividade mega sena


# listaNumero = []
# numero=""

# def GeraJogos():
#     while len(listaNumero)!=6:
#         numero=random.randint(1,60)
        
#         if numero not in listaNumero:
#             listaNumero.append(numero)

#     return listaNumero    


# for i in range(1,6):
#     print(f"APOSTA {i}" , GeraJogos() )
#     listaNumero.clear()



















