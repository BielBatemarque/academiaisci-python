try: 
    numero = int(input('digite um numero: '))
except:
    print('valor invalido')

if numero < 0:
    print('numero negativo')

numero = str(numero)
numero = numero[-1]
numero = int(numero)

if numero%2 == 0:
    print('numero par')
else:
    print('numero impar')
print(numero)