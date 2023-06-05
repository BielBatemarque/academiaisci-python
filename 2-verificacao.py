from datetime import date
nome = ""
idade = 0

nome = input('digite seu nome: ')
idade = int(input('digite sua idade:'))

date = date.today()
ano_atual = date.year
ano_nascimento = ano_atual - idade

print(f"{nome}, voce tem {idade} anos e nasceu em {ano_nascimento}")

if idade < 18:
    print('menor de idade')