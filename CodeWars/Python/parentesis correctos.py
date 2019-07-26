def valid_parentheses(string):
    if len(string) < 1 or len(string) > 99:
        return False
    pila = []
    

def switch(caracter):
    switcher = {
        1: ')',
        2: ']',
        3: '}',
        4: '>',
        5: '(',
        6: '[',
        7: '{',
        8: '<',
        9: False
    }
    print switcher.get(caracter, "Caracter no válido")

switch('f')