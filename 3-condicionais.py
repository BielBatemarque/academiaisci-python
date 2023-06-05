from datetime import date

idade = int(input('> Digite sua idade: '))
date = date.today()
anoAtual = date.year
anoNascimento = anoAtual - idade
geracao = ''

if anoNascimento > 1946 and anoNascimento <1964:
    geracao = 'Boomers'
elif anoNascimento > 1965 and anoNascimento < 1980:
    geracao = 'Geracao X'
elif anoNascimento > 1981 and anoNascimento < 1996: 
    geracao = 'Milenial'
elif anoNascimento > 1997 and anoNascimento < 2012:
    geracao = 'Geracao Z'
elif anoNascimento > 2012:
    geracao = 'Geracao alpha'
else:
    geracao = 'idoso'

print(f'voce tem {idade} anos e é: {geracao}')