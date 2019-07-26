def par_izq():
    return False



def numeros_a_meses(caracter):
    switcher = {
        ')' : par_izq,
        '}' : two,
        ']' : three,
        '>' : four
    }
    return switcher.get(caracter)
    
print(numeros_a_meses(')'))