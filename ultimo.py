contador = 0 
suma = 0
maximo = 0
minimo = 0
primerNumero = True
while True:
    try:
        numero = input("Ingrese un numero: ")
        if (numero == "salir"):
            break
        else:
            suma = suma + int(numero)
            contador = contador + 1
            promedio = suma / contador
            if (primerNumero):
                minimo = int(numero)
                maximo = int(numero)
                primerNumero = False
            else:
                if (int(numero) > maximo): maximo = int(numero)
                if (int(numero) < minimo): minimo = int(numero)
    except:
        print("Error, debe ingresar un valor numérico")
        contador = contador - 1
        continue
print("Máximo:", maximo)
print("Mínimo:", minimo)