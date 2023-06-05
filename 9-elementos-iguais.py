principal = [175, 235, 935, 25, 450, 650]
secundaria = [340, 450, 75, 95, 175, 10]
iguais = []

for i in principal:
    for j in secundaria:
        if i == j:
            iguais.append(i)

print(iguais)