mensagem = input('digite uma mensagem: ')

for char in reversed(mensagem):
    char_lower = char.lower()

    if char_lower == "a" or char == "e" or char == "i" or char == "u" or char == "o":
        continue

    if char.isdigit():
        break
    
    print(char)