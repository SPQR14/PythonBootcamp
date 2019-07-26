def valid_parentheses(string):
    if len(string) <= 0:
        return True
    elif len(string) >= 100:
        return True
    else:
        return validacion(string)


def validacion(cadena):
    print("holi")
    return True

  
print(valid_parentheses("Holo"))