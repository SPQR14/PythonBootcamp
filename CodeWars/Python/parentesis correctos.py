def valid_parentheses(string):
    if len(string) < 0 or len(string) > 100:
        return False
    else:
        return validacion(string)
        
def validacion(string):
    if len(string) % 2 == 0:
        return True
    else:
        return False
    return False

print(valid_parentheses("()()()()()()(())"))