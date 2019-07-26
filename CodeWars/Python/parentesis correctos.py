def valid_parentheses(string):
    if len(string) < 1 or len(string) > 99:
        return False
    pila = []