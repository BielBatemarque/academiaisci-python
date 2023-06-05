def isPalindromo(frase):
    '''
        verifca se a string usada é um paliundromo
    '''
    letras = ''
    fraseModificada = frase.replace(' ', '')
    fraseModificada = fraseModificada.replace(',', '')
    for i in fraseModificada :
        letras += i

    letasAoContrario = letras[::-1]

    if letras == letasAoContrario:
        return True
    else:
        return False
    
print(isPalindromo('luz, azul'))