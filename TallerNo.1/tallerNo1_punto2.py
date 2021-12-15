import math

def funcion (x):
    resultado=0
    if x%4==0:
        resultado=math.pow(x,2)
    elif x%4==1:
        resultado=x/6
    elif x%4==2:
        resultado=math.sqrt(x)
    elif x%4==3:
        resultado=math.pow(x,3)+5
    return resultado

print(funcion(7))