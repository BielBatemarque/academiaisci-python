while True:
    numero = input("Digite um número inteiro (ou 'sair' para sair): ")

    if numero.lower() == "sair":
        print("Programa encerrado.")
        break

    try:
        numero = int(numero)

        inverso = int(str(numero)[::-1])
        print("O inverso de", numero, "é", inverso)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")