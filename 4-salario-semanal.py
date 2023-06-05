nome = input('informe o nome do funcionario: ')
valorHora = float(input('informe o valor da hora trabalhada: '))
horas = int(input('informe a quantidade de horas trabalhadas: '))

qtnHorasExtras = 0
valorHoraExtra = 0
if horas > 44:
    qtnHorasExtras = horas - 44
    valorHoraExtra = valorHora * 1.50

salarioTotal = ((valorHora * horas) + (valorHoraExtra * qtnHorasExtras)) * 4

print(f"{nome} fez {qtnHorasExtras} horas extras com o valor de {valorHoraExtra} cada hora, seu salario total foi de {salarioTotal}")

