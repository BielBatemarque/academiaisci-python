numero = float(input('informe um numero par: '))
print(numero)

while numero % 2 != 0 or numero < 0:
    numero = float(input('informe um numero par: '))
    
while numero/2 > 50:
    numero /= 2
    print(numero)