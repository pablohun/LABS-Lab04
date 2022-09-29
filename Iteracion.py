contador = 0 
suma = 0
while True:
    try:
        numero = input("Ingrese un numero: ")
        if (numero == "salir"):
            break
        else:
            suma = suma + int(numero)
            contador = contador + 1
            promedio = suma / contador
    except:
        print("Error, debe ingresar un valor numerico")
        contador = contador -1
        continue
print("Contador:", contador)
print("Suma:", suma)
print("Promedio:", suma/contador)