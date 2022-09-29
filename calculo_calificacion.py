def calcularGrade(score):
    if(float(score) >= 0.9 and float(score) <= 1.0):
        print("Sobresaliente")
    elif(float(score) >= 0.8 and float(score) < 0.9):
        print("Notable")
    elif(float(score) >= 0.7 and float(score) < 0.8):
        print("Bien")
    elif(float(score) >= 0.6 and float(score) < 0.7):
        print("Suficiente")    
    elif(float(score) >= 0 and float(score) < 0.6):
        print("Insuficiente")
    else:
        print("Score no es valido")
    return score

while True:
    score = input("Ingrese la clasificacion (0.01-1.00): ")
    if(score == "done"):
        break
    calcularGrade(score)
