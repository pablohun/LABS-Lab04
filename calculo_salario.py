def calcularSalario(horas, tarifa):
    horas_extras = horas - MAX_HORAS_SEMANALES
    if (horas_extras > 0):
        pago = (MAX_HORAS_SEMANALES * tarifa) + (horas_extras * (tarifa * 1.5))
    else:
        pago = horas * tarifa
    return pago

try:
    MAX_HORAS_SEMANALES = 40
    horas = int(input("Ingrese numero de horas: "))
    tarifa = float(input("Ingrese tarifa por hora: "))
    salario = calcularSalario(horas, tarifa)
    print(salario)
except:
    print("Error, debe ingresar un número")