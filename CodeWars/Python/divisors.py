def divisors(integer):
    arr = []
    for x in range(2,integer - 1): #if integer is 12
        if integer % x == 0:
            arr.append(x)

    if len(arr) == 0:
        return str(integer) + ' is prime'
    else:    
        return(arr) 