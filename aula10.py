import os 
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

