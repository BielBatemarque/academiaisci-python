numero = int(input('Digite um numero inteiro: '))

numeroNegativo = False

if numero < 0:
    numeroNegativo = True

numeroString = str(numero)
if numeroNegativo:
    numeroString = numeroString[1:]

numeroInvertido = ""
indiceAtual = len(numeroString) - 1

for char in reversed(numeroString):
    numeroInvertido += char

print(numeroInvertido)