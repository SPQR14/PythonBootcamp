def next_bigger(num):
    lst_num = [int(i) for i in str(num)]

    indice_para_reemplazo = -1
    i = len(lst_num) - 1
    #Partir la cadena en dos partes, lo que te decía de la tercera validación
    #es el índide menos 1, para tomar el que sigue y no caer en el error
    while i > 0:
        if lst_num[i] > lst_num[i-1]:
            indice_para_reemplazo = i - 1
            break
        i -= 1

    if indice_para_reemplazo == -1:
        return -1
    else:
        derecha = lst_num[:indice_para_reemplazo]
        reemplazo = lst_num[indice_para_reemplazo]
        izquierda = lst_num[indice_para_reemplazo+1:]
        nueva_reemplazo = 9
        i = 0
        borrado = 0
        while i < len(izquierda):
            if izquierda[i] > reemplazo and izquierda[i] < nueva_reemplazo:
                nueva_reemplazo = izquierda[i]
                borrado = i
            i += 1

        izquierda.pop(borrado)
        izquierda.append(reemplazo)
        derecha.append(nueva_reemplazo)
        salida = derecha + sorted(izquierda)
        return int(''.join(str(x) for x in salida))

print(next_bigger('2321'))