import math

def compara_numeros(a,b):
    if b == math.pow(a,2):
        print("El segundo es el cuadrado exacto del primero")
    elif b < math.pow(a,2):
        print("El segundo es menor que el cuadrado del primero")
    elif b > math.pow(a,2):
        print("El segundo es mayor que el cuadrado del primero")

compara_numeros(2, 3)