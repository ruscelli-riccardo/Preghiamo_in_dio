lista = [23, 5 , 6 , 900, 0 , 123]
def piùgrande(lista):
    big=0
    for x in lista:
        if x > big:
            big=x
    print(big)

piùgrande(lista)