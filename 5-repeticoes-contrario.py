frase = input('digite uma frase com no minimo 10 caracteres: ')
while len(frase) < 10:
    frase = input('digite uma frase com no minimo 10 caracteres: ')


counter = (len(frase))
while counter != 0:
    counter-= 1
    print(f"{frase[counter]}")