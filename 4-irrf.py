salario = float(input('informe seu salário: '))
aliquota = 0
desconto = 0

if salario < 1903.98:
    aliquota = 0
    desconto = 0
elif salario < 2826.65:
    aliquota = 0.075
    desconto = 142.80
elif salario < 3751.04:
    aliquota = 0.15
    desconto = 354.80
elif salario < 4664.67:
    aliquota = 0.225
    desconto = 636.13
else:
    aliquota = 0.275
    desconto = 869.36

print(f"o imposto deve a aliquota de: {aliquota * 100}% com o valor de: {(salario * aliquota) - desconto}")