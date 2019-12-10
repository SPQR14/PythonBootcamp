def number(bus_stops):
    aux0 = []
    aux1 = []
    total = 0
    for i in range(0, len(bus_stops) + 1):
        aux0 = bus_stops[i]
        print(aux0)
        aux1 = bus_stops[i + 1]
        print(aux1)
        total += aux0[0] + aux1[0] - aux1[1]
        print(total)
    return total

print(number([[10,0],[3,5],[5,8]]))