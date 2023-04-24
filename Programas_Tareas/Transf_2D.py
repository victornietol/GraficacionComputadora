import matplotlib.pyplot as plt
import math

def graficar_puntos(x,y):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    plt.plot(x,y,"o")
    plt.show()
    
def graficar_linea(x,y):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.plot(x,y)
    plt.show()

def escalar(x,y,s):
    for i in range(len(x)):
        x[i]=x[i]*s
        y[i]=y[i]*s
    return x,y
    #graficar_puntos(x,y)

def trasladar_origen(x,y,pivote):
    for i in range(len(x)):
        x[i]= x[i]+(-pivote[0])
        y[i]= y[i]+(-pivote[1])
    return x,y

def trasladar_regresar(x,y,pivote):
    for i in range(len(x)):
        x[i]= x[i]+(pivote[0])
        y[i]= y[i]+(pivote[1])
    return x,y

def rotar(x,y,angulo):
    radianes = math.radians(angulo)
    rotacion = [[math.cos(radianes), -math.sin(radianes)] , [math.sin(radianes), math.cos(radianes)]]
    for i in range(len(x)):
        punto = [x[i],y[i]]  # Almacenando el punto para poder manipularlo después
        punto[0] = (rotacion[0][0]*x[i])+(rotacion[0][1]*y[i])  # Rotacion de x
        punto[1] = (rotacion[1][0]*x[i])+(rotacion[1][1]*y[i])  # Rotacion de y
        x[i], y[i] = punto[0], punto[1]
    return x,y


x=[20,60,40,40]
y=[20,20,60,40]
s=0.30
grados=[30,33,68,55]
pivotes=[3,0,1,2] # Llevar el control de cual pivote toca 


#graficar_puntos(x, y)
x,y = escalar(x, y, s)
graficar_puntos(x, y)

"""  -- Forma individual
# Rotando figura
x,y = trasladar_origen(x, y, [12,12])
x,y = rotar(x, y, 30)
x,y = trasladar_regresar(x, y, [12,12])

graficar_puntos(x, y)
"""
piv_aux = 0
for g in grados:
    pivote = pivotes[piv_aux] # Seleccionando pivote
    punto_piv = [x[pivote],y[pivote]]
    x,y = trasladar_origen(x, y, punto_piv)
    x,y = rotar(x, y, g)
    x,y = trasladar_regresar(x, y, punto_piv)
    
    graficar_puntos(x, y)
    piv_aux +=1