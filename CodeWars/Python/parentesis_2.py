def valid_parentheses(string):
    string = string.replace(" ", "")
    pila = []
    val = False
    car = None
    carP = None
    for x in range(0,len(string)):
        carP = string[x]
        if carP == '(':
            pila.append(')')
        else:
            if carP == '[':
                pila.append(']')
            else:
                if carP == '{':
                    pila.append('}')
                else:
                    if carP == '<':
                        pila.append('>')
                    else:
                        # Parte falsa
                        if carP == ')':
                            if not pila:
                                val = False
                            else:
                                car = pila.pop()
                                if car != ')':
                                    val = False
                                else:
                                    val = True
                        else:
                            if carP == ']':
                                if not pila:
                                    val = False
                                else:
                                    car = pila.pop()
                                    if car != ']':
                                        val = False
                                    else:
                                        val = True
                            else:
                                if carP == '}':
                                    if not pila:
                                        val = False
                                    else:
                                        car = pila.pop()
                                        if car != '}':
                                            val = False
                                        else:
                                            val = True
                                else:
                                    if carP == '>':
                                        if not pila:
                                            val = False
                                        else:
                                            car = pila.pop()
                                            if car != '>':
                                                val = False
                                            else:
                                                val = True
                                    
        if not val:
            break
    
    return val


print(valid_parentheses("(g)s(ox)m(s)"))