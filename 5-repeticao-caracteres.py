frase = input('digite uma frase com no minimo 10 caracteres: ')
while len(frase) < 10:
    frase = input('digite uma frase com no minimo 10 caracteres: ')


counter = 0
while counter < len(frase):
    print(f"{frase[counter]}")
    counter+= 1