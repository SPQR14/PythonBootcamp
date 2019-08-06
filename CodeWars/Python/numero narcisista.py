def narcissistic( value ):
    cad = str(value)
    lst_num = [int(i) for i in str(cad)]
    cifras = len(lst_num)
    for i in range(0, len(lst_num)):
        lst_num[i] = (lst_num[i] ** cifras)
    if value == (sum(lst_num)):
        return True
    else:
        return False


print(narcissistic(153))