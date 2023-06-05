soma = 0

while soma < 500 :
    try:
        numero = float(input('digite um numero: '))
    except:
        print('valor informado incorreto')
    soma += numero
