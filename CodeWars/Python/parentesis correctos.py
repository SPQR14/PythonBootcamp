def valid_parentheses(string):
    if len(string) < 1 or len(string) > 99:
        return False
    pila = []
    

def switch(caracter):
    switcher = {
        ')': False,
        ']': True,
        '}': True,
        '>': True,
        '(': '(',
        '[': '[',
        '{': '{',
        '<': '<',
    }
    return switcher.get(caracter)

print(switch(')'))