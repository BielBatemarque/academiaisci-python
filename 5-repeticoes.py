numero = 0
limitador = float(input('informe o limite de digitos: '))

while numero < limitador:
    numero = numero + 1

    ultimoNumero = str(numero)[-1]
    if numero %2 == 1 and ultimoNumero != "5":
        continue

    print(numero)