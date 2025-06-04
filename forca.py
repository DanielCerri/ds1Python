#atividade da forca
import os
os.system("cls")
desenhoForca = ['''
+---+
    |
    |
    |
    |
    |
=========''',
'''
+---+
|   |
    |
    |
    |
    |
=========''','''

+---+
|   |
O   |
    |
    |
    |
=========''','''

+---+
|   |
O   |
|   |
    |
    |
=========''','''

+---+
|   |
O   |
/|   |
    |
    |
=========''','''

+---+
|   |
O   |
/|\  |
    |
    |
=========''','''

+---+
|   |
O   |
/|\  |
/    |
    |
=========''','''

+---+
|   |
O   |
/|\  |
/ \  |
    |
=========''']

#operadores condicionais > >= < <= == != and or in not in
palavra =  list(input("Digite uma palavra: "))
quantidade=["_"]*len(palavra)
ganhou=False

input("Digite enter para continuar...")
os.system("cls")

print(desenhoForca[0])
print(f"Palavra de {len(quantidade)} letras")
print(quantidade)
erro = 0 

while erro!=7:

    letra=input("Digite uma letra:")
    print(quantidade)

    if letra in palavra:
        
        for i in range(len(palavra)):
           
           if letra == palavra[i]:
               quantidade[i]=letra
        else:
            print(quantidade)

    else:
        erro +=1
        print(desenhoForca[erro])
        print(f"Faltam {7-erro} tentativas")

    if "_" not in quantidade:
        ganhou=True
        erro=7
    
else:

    if ganhou==True:
        print("ganhou")
    else:
        print("perdeu")





nums = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1] 

contar = nums.count(0)