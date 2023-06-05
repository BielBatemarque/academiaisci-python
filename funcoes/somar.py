def somar(a,b):
    if type(a) != int or type(b) != int:
        raise Exception("A função só aceita tipos numericos inteiros")
    if a < 9 and b < 9:
        raise Exception('A função só pode somar numeros maiores ou iguais a 10')
    return a + b