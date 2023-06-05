def separador(frase, separador):
    arr = []
    termo = ''

    for i in frase:
        if i != separador:
            termo += i
        elif termo:
            arr.append(termo)
            termo = ''
    
    if termo:
        arr.append(termo)

    return arr

        


print(separador('casa-carro', '-'))