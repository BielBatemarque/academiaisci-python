from funcoes.somar import somar
from funcoes.dividir import dividir
from funcoes.multiplicar import multiplicar
from funcoes.subtrair import subtrair

def realizaOperacao(sinal, n1, n2):
    if sinal == '+':
        return n1 + n2
    elif sinal == '-':
        return n1 - n2
    elif sinal == '*':
        return n1 * n2
    elif sinal == '/':
        return n1/n2
    

operacao = input('digite a operação (+, -, *, /): ')
primeiroNumero = float(input('> digite o primeiro Numero: '))
segundoNumero = float(input('> digite o segundo Numero: '))

print(realizaOperacao(operacao, primeiroNumero, segundoNumero))