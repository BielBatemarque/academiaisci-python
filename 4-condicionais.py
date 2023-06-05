import sys

try:
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    nota3 = float(input('digite a terceira nota: '))
except:
    print('valor informado incorreto')
    sys.exit(0)
media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print('Aprovado')
else:
    try:
        notaRecuperacao = float(input('digite a nota da recuperação: '))
    except:
        print('valor informado incorreto')
        sys.exit(0)
    if notaRecuperacao == 0:
        print('Reprovado, sem recuperação')
    elif notaRecuperacao < 8:
        print('reprovado, com recuperação')
    else:
        print('Aprovado com recuperação')
