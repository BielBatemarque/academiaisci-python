def verificar_mascara(string, mascara):
    if len(string) != len(mascara):
        return False
    
    for s, m in zip(string, mascara):
        if m == '*':
            continue
        elif m != s:
            return False
    
    return True

print(verificar_mascara('(123) 456-7890', '(***) ***-****'))  # True