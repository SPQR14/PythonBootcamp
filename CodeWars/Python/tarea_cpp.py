import math

def cubo():
    print("Cubo")
    l = float(input("Ingresa la medida del lado: "))
    print("El volumen es: ")
    return l**3

def cilindro():
    print("Cilindro")
    r = float(input("ingresa la medida del radio de la base: "))
    h = float(input("ingresa la medida de la altura: "))
    print("El volumen es: ")
    return math.pi * r**2 * h

def piramide():
    print("Pirámide")
    l = float(input("ingresa la medida del lado: "))
    h = float(input("ingresa la medida de la altura: "))
    print("El volumen es: ")
    return (l**2 * h) / 2

def cono():
    print("Cono")
    r = float(input("Ingresa la medida del radio de la base: "))
    h = float(input("Ingresa la medida de la altura: "))
    print("El volumen es: ")
    return (math.pi * r**2 * h) / 3

def cuadrado():
    print("Cuadrado")
    l = float(input("Ingresa la medida del lado: "))
    print("El área es: ")
    return l**2

def rectangulo():
    print("Rectángulo")
    b = float(input("Ingresa la medida de la base: "))
    h = float(input("Ingresa la medida de la altura: "))
    print("El área es: ")
    return h * b

def triangulo():
    print("Triángulo")
    b = float(input("Ingresa la medida de la base: "))
    h = float(input("Ingresa la medida de la altura: "))
    print("El área es: ")
    return (b * h) / 2

def circulo():
    print("Circulo")
    r = float(input("Ingresa la medida del radio: "))
    print("El área es: ")
    return math.pi * r**2

def menu_principal(des):
    print("Selecciona una opcion")
    print("1. Calcular volumen")
    print("2. Calcular area")
    print("3. Salir")
    while True:
        des = int(input("Opción"))
        if des < 1 or des > 3:
            print("Opción incorrecta")
            des = menu_principal(des)
        if des >= 1 or des <= 3:
            break
    return des

def menu_voumen():
    print("Calcular volumenes")
    print("Selecciona una opción")
    print("1. Cubo")
    print("2. Cilindro")
    print("3. Piramide")
    print("3. Cono")
    while True:
        des = int(input("Opción"))
        if des < 1 or des > 4:
            print("Opción incorrecta")
            des = menu_principal(des)
        if des >= 1 or des <= 4:
            break
    if des == 1:
        print(cubo())
    elif des == 2:
        print(cilindro())
    elif des == 3:
        print(piramide())
    elif des == 4:
        print(cono())
    else:
        print("Chaaaaato")
    
def menu_area():
    print("Calcular áreas")
    print("Selecciona una opción")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("3. Círculo")
    while True:
        des = int(input("Opción"))
        if des < 1 or des > 4:
            print("Opción incorrecta")
            des = menu_principal(des)
        if des >= 1 or des <= 4:
            break
    if des == 1:
        print( cuadrado() )
    elif des == 2:
        print(rectangulo())
    elif des == 3:
        print(triangulo())
    elif des == 4:
        print(circulo())
    else:
        print("Chaaaaato")
    
def main():
    des = 0
    while True:
        des = menu_principal(des)
        if des == 1:
            menu_voumen()
        elif des == 2:
            menu_area()
        else:
            print("Sale bye")
            break

main() 