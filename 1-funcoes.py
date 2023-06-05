def somar(list):
    contador = 0
    for i in list:
        contador += i
    return contador/len(list)

print(somar([5,8,10]))