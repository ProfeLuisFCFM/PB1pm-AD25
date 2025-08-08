anio = int(input("Ingrese un año válido: "))

if anio < 0:
    anio = int(input("Ingrese un año válido: "))
else:
    if anio % 4 == 0:
        print("El año:",anio ,"es un Año Bisiesto")
    elif anio % 100 != 0 and anio % 400 == 0:
        print("El año:",anio ,"es un Año Bisiesto")
    else:
        print("El año:",anio ,"NO es un Año Bisiesto")

