condicao = True
numeros = []
maior = 0


while condicao:
    numero = input('Digite um numero: ')
    if numero == 'sair' :
        condicao = False
        break
    numeros.append(int(numero))

for i in numeros:
    if i > maior:
        maior = i

print(f'a lista foi {numeros} e o maior foi {maior}')
