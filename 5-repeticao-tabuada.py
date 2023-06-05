numero = float(input('insira um numero para obter sua tabuada: '))
for i in range(10):
    print(f'{numero} x {i + 1} = {numero * (1 + i)}')