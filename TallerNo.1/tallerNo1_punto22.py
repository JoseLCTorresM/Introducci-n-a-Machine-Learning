import math

def calcularArea(l1,l2,angulo):
    grados = angulo * math.pi/180
    Area=(1/2*l1*l2)*math.sin(grados)
    return f"El área compuesta por los lado de {l1} mtrs y {l2} mtrs, y el angulo de {angulo}° es de {Area} mtrs"

def conversor (medida, numero_transformar):
    numero_deseado = 0
    if medida == "metros" :
        numero_deseado = numero_transformar*1/1000
        print (f"Su número, de centimetros a metros, es {numero_deseado}")
    elif medida == "centimetros":
        numero_deseado = numero_transformar*1000
        print (f"Su número, de metros centimetros, es {numero_deseado}")
    else:
        print("Unidad métrica no soportada")

'''
--------------------------------------------------------------------------------------------------------------------------
'''

#conversor(input("Pasar a metros o a centimetros: "), float(input("Digite su número: ")))

print(calcularArea(float(input("Digite lado #1 (en metros): ")), float(input("Digite lado #2 (en metros): ")), float(input("Digite angulo (en grados): "))))
