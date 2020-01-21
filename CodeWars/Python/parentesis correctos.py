def valid_parentheses(string):
    string = string.replace(" ", "")
    if len(string) % 2 != 0:
        return False
    elif not string:
        return True
    else:
        pila = []
        val = True
        car = None
        for x in range(0,len(string)):
            if string[x] == '(':
                pila.append(')')
            elif string[x] == '[':
                pila.append(']')
            elif string[x] == '{':
                pila.append('}')
            elif string[x] == '<':
                pila.append('>')
            elif string[x] == ')':
                car = pila.pop()
                if car != ')':
                    val = False
                else:
                    val = True
            elif string[x] == ']':
                car = pila.pop()
                if car != ']':
                    val = False
                else:
                    val = True
            elif string[x] == '}':
                car = pila.pop()
                if car != '}':
                    val = False
                else:
                    val = True
            elif string[x] == '>':
                car = pila.pop()
                if car != '>':
                    val = False
                else:
                    val = True
            if not val:
                break
        
        if not pila:
            return True
        else:
            return False



"""
def validacion(string):
    string = string.replace(" ", "")
    if len(string) % 2 != 0:
        return False
    elif not string:
        return True
    else:
        pila = []
        val = True
        car = None
        for x in range(0,len(string)):
            if string[x] == '(':
                pila.append(')')
            elif string[x] == '[':
                pila.append(']')
            elif string[x] == '{':
                pila.append('}')
            elif string[x] == '<':
                pila.append('>')
            elif string[x] == ')':
                car = pila.pop()
                if car != ')':
                    val = False
                else:
                    val = True
            elif string[x] == ']':
                car = pila.pop()
                if car != ']':
                    val = False
                else:
                    val = True
            elif string[x] == '}':
                car = pila.pop()
                if car != '}':
                    val = False
                else:
                    val = True
            elif string[x] == '>':
                car = pila.pop()
                if car != '>':
                    val = False
                else:
                    val = True
            if not val:
                break
        
        if not pila:
            return True
        else:
            return False
"""

print(valid_parentheses(""))

