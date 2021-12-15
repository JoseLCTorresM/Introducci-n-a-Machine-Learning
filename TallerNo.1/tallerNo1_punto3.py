def doble_de_un_impar ():
    x=int(input("Digite un numero entero: "))
    if (x/2)%2==1:
        print(f"{x} es el doble de un numero impar")
    else:
        print(f"{x} no es el doble de un numero impar")
        
doble_de_un_impar()