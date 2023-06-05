numeros = []
media = 0
for i in range(3):
    numeros.append(int(input('insira um numero: ')))
    media += numeros[i]

print(media/3)