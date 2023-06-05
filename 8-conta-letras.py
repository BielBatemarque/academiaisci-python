palavras = []
contador = 0

for i in range(3):
    palavra = input('Informe uma palavra: ')
    palavras.append(palavra)

letra = input('informe uma letra: ')

for palavra in palavras:
    for i in palavra:
        if letra == i:
            contador += 1

print(f'a letra {letra} está {contador}x nas palavras digitadas')
