def desenhar_retangulo(altura, largura, caractere):
    for i in range(altura):
        for j in range(largura):
            print(caractere, end='')
        print()

altura = int(input("Digite a altura do retângulo: "))
largura = int(input("Digite a largura do retângulo: "))
caractere = input("Digite o caractere para desenhar o retângulo: ")

desenhar_retangulo(altura, largura, caractere)