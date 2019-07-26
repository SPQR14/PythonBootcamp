def par_izq():
    return "Hola"

def two():
    return True

def three():
    return False

def four():
    return False


def numeros_a_meses(caracter):
    switcher = {
        ')' : par_izq,
        '}' : two,
        ']' : three,
        '>' : four
    }
    func = switcher.get(caracter, lambda: "Invalid char")
    return func()

print(numeros_a_meses(''))