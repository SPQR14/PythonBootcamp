def high_and_low(numbers):
    numbers = numbers.split()
    lst_numbers = [int(i) for i in numbers]
    lst_numbers.sort()
    return str(lst_numbers[-1]) + " " + str(lst_numbers[0])

    
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))