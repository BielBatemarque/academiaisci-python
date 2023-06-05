meias = [
    "vermelha", "vermelha", "roxa",
    "vermelha", "azul", "amarela",
    "roxa", "azul", "vermelha",
    "roxa", "roxa", "azul",
    "vermelha", "amarela", "amarela",
    "vermelha", "roxa", "vermelha",
    "amarela", "roxa", "roxa"
]

cores = {}
Tpares = 0

for cor in meias:
    if cor in cores:
        cores[cor] += 1
    else:
        cores[cor] = 1

for cor, qtn in cores.items():
    par = qtn // 2
    sobras = qtn % 2
    cores[cor] = par
    Tpares += par

print("quantidade total de meias:", Tpares)
for cor, par in cores.items():
    print("Cor:", cor, "- Pares:", par, "- Sobras:", sobras)