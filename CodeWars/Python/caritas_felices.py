def count_smileys(arr):
    aux = None
    cont = 0
    ojos = False
    boca = False
    for i in range(0, len(arr) - 1):
        aux = arr[i]
        if len(aux) > 3:
            continue
        if not aux:
            continue
        if aux[0] == ':' or aux[0] == ';':
            ojos = True
        if aux[-1] == ')' or aux[-1] == 'D':
            boca = True
        if boca == True and ojos == True:
            cont += 1
        ojos = boca = False
    return cont

print(count_smileys(['', ':D']))