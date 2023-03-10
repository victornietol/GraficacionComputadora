# Algoritmo Brensenham

import matplotlib.pyplot as plt
import numpy as np
    
def linea_vertical(punto1,punto2,pk):
    # Acomodando puntos para revisarlos de abajo hacia arriba
    if(punto1[1]>punto2[1]):
        aux = punto2
        punto2 = punto1
        punto1 = aux
    # Inicio del proceso    
    puntos,pk_lista=[],[]
    puntoActual=[punto1[0],punto1[1]]
    final=[punto2[0],punto2[1]]
    while (puntoActual[1]!=final[1]):
        puntoActual[1] +=1
        puntos.append((puntoActual[0],puntoActual[1]))
        pk_lista.append("--")
    return puntos,pk_lista,punto1      
        
def linea_horizontal(punto1,punto2,pk):
    puntos,pk_lista=[],[]
    puntoActual=[punto1[0],punto1[1]]
    final=[punto2[0],punto2[1]]
    while (puntoActual[0]!=final[0]):
        puntoActual[0] +=1
        puntos.append((puntoActual[0],puntoActual[1]))
        pk_lista.append("--")
    return puntos,pk_lista      
    
def diagonal_positiva(punto1,punto2,pk,deltaX,deltaY):
    puntos,pk_lista = [],[]
    puntoActual=[punto1[0],punto1[1]]
    final=[punto2[0],punto2[1]]
    while(puntoActual!=final):
        if(pk < 0):
            puntoActual[0]+=1
            puntos.append((puntoActual[0],puntoActual[1]))
            pk_lista.append(pk)
            pk += 2*deltaY              
        elif(pk > 0):
            puntoActual[0]+=1
            puntoActual[1]+=1
            puntos.append((puntoActual[0],puntoActual[1]))
            pk_lista.append(pk) 
            pk += (2*deltaY) - (2*deltaX)
    return puntos,pk_lista

def diagonal_negativa(punto1,punto2,pk,deltaX,deltaY):
    puntos,pk_lista = [],[]
    puntoActual=[punto1[0],punto1[1]]
    final=[punto2[0],punto2[1]]
    while(puntoActual!=final):
        if(pk < 0):
            puntoActual[1]-=1            
            puntos.append((puntoActual[0],puntoActual[1]))
            pk_lista.append(pk) 
            pk += 2*deltaX
        elif(pk > 0):
            puntoActual[0]+=1
            puntoActual[1]-=1  
            puntos.append((puntoActual[0],puntoActual[1]))
            pk_lista.append(pk) 
            pk += (2*deltaX) - (2*deltaY)
    return puntos,pk_lista    
      
def graficar(deltaX,deltaY,puntos,punto1,direccion):
    # Generando una matriz donde se van a poner los puntos
    imagen = np.ones((deltaY+10,deltaX+10)) # Para que la imagen no quede tan justa
    fig, ax = plt.subplots()
    
    # Asignando los puntos que se van a pintar
    if(direccion=="positiva"):
        x,y = 5,5   # Puntos iniciales que se van a pintar 
    elif(direccion=="negativa"):
        x,y = 5,deltaY  # Puntos iniciales que se van a pintar 
        
    imagen[y,x] = 0   # Inicio
    
    for i in range(len(puntos)):
        # Apartir del segundo punto
        if(i>0):       
            # Verificando si los puntos avanzan, disminuyen o se quedan igual para pintar el siguente cuadro
            if(puntos[i][0]>puntos[i-1][0]) and (puntos[i][1]>puntos[i-1][1]):  # Si avanzan los dos
                x +=1
                y +=1
                imagen[y,x] = 0
            elif(puntos[i][0]>puntos[i-1][0]): # Si avanza x
                x +=1
                imagen[y,x] = 0
            elif(puntos[i][1]>puntos[i-1][1]): # Si avanza y
                y +=1
                imagen[y,x] = 0
            elif(puntos[i][0]<puntos[i-1][0]) and (puntos[i][1]<puntos[i-1][1]):  # Si retroceden los dos
                x -=1
                y -=1
                imagen[y,x] = 0
            elif(puntos[i][0]<puntos[i-1][0]): # Si retrocede x
                x -=1
                imagen[y,x] = 0
            elif(puntos[i][1]<puntos[i-1][1]): # Si retrocede y
                y -=1
                imagen[y,x] = 0
        # Primer punto
        else:
            # Verificando si los puntos avanzan, disminuyen o se quedan igual para pintar el siguente cuadro
            if(puntos[i][0]>punto1[0]) and (puntos[i][1]>punto1[1]):  # Si avanzan los dos
                x +=1
                y +=1
                imagen[y,x] = 0
            elif(puntos[i][0]>punto1[0]): # Si avanza x
                x +=1
                imagen[y,x] = 0
            elif(puntos[i][1]>punto1[1]): # Si avanza y
                y +=1
                imagen[y,x] = 0
            elif(puntos[i][0]<punto1[0]) and (puntos[i][1]<punto1[1]):  # Si retroceden los dos
                x -=1
                y -=1
                imagen[y,x] = 0
            elif(puntos[i][0]<punto1[0]): # Si retrocede x
                x -=1
                imagen[y,x] = 0
            elif(puntos[i][1]<punto1[1]): # Si retrocede y
                y -=1
                imagen[y,x] = 0

    ax.imshow(imagen,vmin=0,vmax=1,origin="lower",cmap="gray")
    ax.set_aspect("equal")

def graf2(puntos):
    x,y=[],[]
    for v in puntos:
        x.append(v[0])
        y.append(v[1])
    plt.plot(x,y,"r")
    plt.show()
    
# Ejecución del algoritmo
def  alg_Brasenham(punto1,punto2):
    # Acomodando puntos para revisarlos de izquierda a derecha
    if(punto1[0]>punto2[0]):
        aux = punto2
        punto2 = punto1
        punto1 = aux
        
    # Valores
    deltaY = abs(punto1[1]-punto2[1]) # Diferencia de y
    deltaX = abs(punto1[0]-punto2[0]) # Diferencia de x
    dosDeltaY = deltaY*2
    pk = (2*deltaY) - (deltaX)
    
    # Verificando si linea es vertical, horizontal o diagonal para obtener puntos
    if(punto1[0]==punto2[0]):  # Vertical
        puntos,pk,punto1 = linea_vertical(punto1,punto2,pk)
        direccion = "positiva"
    elif(punto1[1]==punto2[1]):  # Horizontal
        puntos,pk = linea_horizontal(punto1,punto2,pk)
        direccion = "positiva"
    elif(punto1[1]<punto2[1]): # Pendiente positiva
        puntos,pk = diagonal_positiva(punto1,punto2,pk,deltaX,deltaY)
        direccion = "positiva"
    elif(punto1[1]>punto2[1]): # Pendiente negativa
        puntos,pk = diagonal_negativa(punto1,punto2,pk,deltaX,deltaY)
        direccion = "negativa"
    
    # Mostrando puntos y pk
    print(f" pk | (x,y)\n------------------\n    | {punto1} ")
    aux=0
    for i in puntos:
        print(f" {pk[aux]} | {i}")
        aux+=1
    print()
                
    # Graficando
    graficar(deltaX, deltaY, puntos, punto1, direccion)

    #graf2(puntos)    
    
# Ingresar los puntos:
# Pendiente positiva
alg_Brasenham((5,5),(30,20))
alg_Brasenham((5,5),(300,200))

# Pendiente negativa
alg_Brasenham((25,25),(40,5))

# Linea vertical
alg_Brasenham((5,5),(5,20))

# Linea horizontal
alg_Brasenham((5,20),(20,20))