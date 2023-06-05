nomeInformado = input('qual o seu nome? ')
idadeInformada = input('qual sua idade: ')

pessoa = {
    "nome": nomeInformado,
    "idade": idadeInformada
}

propiedadeNova = input('digite uma propridade nova: ')
valorNova = input('digite o valor desta propriedade: ')

pessoa[propiedadeNova] = valorNova

print(pessoa)