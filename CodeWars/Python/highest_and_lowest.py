def high_and_low(numbers):
    numbers = numbers.split()
    lst_numbers = [int(i) for i in numbers]
    lst_numbers.sort()
    return str(lst_numbers[-1]) + " " + str(lst_numbers[0])
    
    
    """
    h = lst_numbers[0]
    l = lst_numbers[0]
    for i in range(0, len(lst_numbers)):
        if h < lst_numbers[i]:
            h = lst_numbers[i]
    for j in range(0, len(lst_numbers)):
        if l > lst_numbers[j]:
            l = lst_numbers[j]
    return str(h) + " " + str(l)
    """
    
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))