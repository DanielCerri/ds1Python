#escopo de funcao e variavel

moreira = 0 


def Teste():
    global moreira
    moreira = 1

Teste()
print(moreira) 



