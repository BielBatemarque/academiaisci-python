dicionario = {}

palavra = input('digite uma palavra: ')
for indice in palavra:
    contador = 0
    for conta in palavra:
        if indice == conta:
            contador += 1
            dicionario[indice] = contador

print(dicionario)