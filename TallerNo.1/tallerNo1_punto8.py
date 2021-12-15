from random import randint
import numpy as np

def comparaPuntos (a,b,c,d,e):
    l = [a,b,c,d,e]
    com = 0          #comparador
    tupla = 0       #tupla que retornará
    for i in range(len(l)-1):
        dist = np.sqrt((l[i+1][0]-l[0][0])**2+(l[i+1][1]-l[0][1])**2)
        if com == 0 :
            com = dist
            tupla=l[i+1]
        elif com!=0 and com > dist :
            com=dist
            tupla=l[i+1]
    return f"La coordenada {tupla} es la más cercana a {l[0]}"

a = (randint(-100,100),randint(-100,100))
b = (randint(-100,100),randint(-100,100))
c = (randint(-100,100),randint(-100,100))
d = (randint(-100,100),randint(-100,100))
e = (randint(-100,100),randint(-100,100))

print(comparaPuntos(a,b,c,d,e))
