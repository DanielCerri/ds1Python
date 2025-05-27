import os 
os.system("cls")
#escopo de funcao e variavel

# moreira = 0 


# def Teste():
#     global moreira
#     moreira = 1

# Teste()
# print(moreira) 

#papelaria
borracha=1.20
lapis=1.45
caneta=2.30 
opcao=0
total=0


def menu():
    print("""
1-COMPRAR MATERIAIS
2-MOSTRAR SALDO
3-FINALIZAR CARRINHO
4-SAIR
""")


def Comprar():
    global total
    item= input("O que voce gostaria de comprar: ")
    qtd= int(input("Digite a quantidade: "))

    if item =="lapis": 
        total += lapis*qtd  
    elif item =="caneta":
        total += caneta* qtd
    elif item == "borracha":
        total += borracha*qtd
    else:
        print("OPÇÃO NAO ENCONTRADA!")

    print("PRODUTO ADICIONADO AO CARRINHO!")
    

def SaldoCarrinho():
    global total
    print(f"TOTAL DO CARRINHO R$: {total}")

def FinalizarCarrinho():
    SaldoCarrinho()

    finalizar = 'n'

    while finalizar == 'n':
        parcela =  int(input("Quantas vezes gostaria de parcelar? (até 12x): "))

        for i in range(1,parcela+1):
            print(f"PARCELA {i}-> {total/parcela} ")

        finalizar = input("DESEJA CONFIRMAR A PARCELA?(S/N) ").lower()
        
        if finalizar == "s":
            print("PAGAMENTO EFETUADO! ")
        

menu()


while opcao !=4:  

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        Comprar()
    elif opcao ==2:
        SaldoCarrinho()
    elif opcao ==3:
        FinalizarCarrinho()


