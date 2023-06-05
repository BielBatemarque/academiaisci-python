import sys

numero = input("Fatorial de: ")
if numero == 'sair' :
    sys.exit(0)
else:
    numero = float(numero)

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)