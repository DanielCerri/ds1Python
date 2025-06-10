import os
os.system("cls")
#dicionarios 

#imagine que voce precise cadastrar em um dicionario 
#varios nomes de aluno - como voce poderia resolver isso? 


#estrutura:
#dicionario = {
        #chave : {
                #2: {key:value}           
            #}
#}

# alunos = {
# 1: 
#     {
#     "nome":"DANIEL" , 
#     "profissão":"dev"
#     },
# 2:{
#     "nome":"guilherme",
#     "profissão":"dev" 
# }
# }


# print(alunos)

# for key1  in alunos.keys():
#     print(alunos[key1]["nome"])
#     print(alunos[key1]["profissão"])



#
medicos = {}

for i in range(1,4):
    medicos.update(
        {
         i: {
             "medico":input("Digite o nome do medico: "),
             "especialidade":input("Digite a especialidade: ")
             } 
        }
    )
else:
    print(medicos)