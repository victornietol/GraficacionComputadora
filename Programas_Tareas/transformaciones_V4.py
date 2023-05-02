import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from matplotlib import cm

# Clase para realizar las transformaciones 2D
class Transf_2D:
    def __init__(self,puntos,tipo):
        self.puntos = puntos
        # Aplicando el tipo de transformacion
        if(tipo == "ROTAR"):
            # Seleccionando pivote
            tmp_piv = int(input("Ingresa el indice del punto correspondiente al punto pivote (Ejemplo: 1 para seleccionar x1,y1. Si quiere seleccionar un punto que no sea vértice ingrese el número -1): "))
            if(tmp_piv == -1):  # Si el pivote es un punto diferente a un vértice
                piv_x = float(input("Ingrese el valor del punto pivote en x: "))  # x
                piv_y = float(input("Ingrese el valor del punto pivote en y: "))  # y
                pivote = [piv_x,piv_y]
            else:
                pivote = [puntos[tmp_piv-1][0],puntos[tmp_piv-1][1]] # Seleccionando pivote
            angulo = float(input("Ingresa el ángulo (Solo el valor númerico): "))
            self.puntos = self.rotar(puntos,pivote,angulo)
        elif(tipo == "TRASLADAR"):
            tras_x = float(input("Ingresa el valor de la traslación en x: ")) 
            tras_y = float(input("Ingresa el valor de la traslación en y: ")) 
            self.puntos = self.trasladar(puntos,tras_x,tras_y)
        elif(tipo == "ESCALAR"):
            esca = float(input("Ingresa el valor del escalamiento en decimales: "))
            self.puntos = self.escalar(puntos,esca)
    
    def trasladar(self,puntos,tras_x,tras_y):
        for i in range(len(puntos)):
            puntos[i][0] = puntos[i][0]+(tras_x)  # punto x
            puntos[i][1] = puntos[i][1]+(tras_y)  # punto y
        return puntos
    
    def escalar(self,puntos,esca):
        for i in range(len(puntos)):
            puntos[i][0] = puntos[i][0]*esca  # punto x
            puntos[i][1] = puntos[i][1]*esca  # punto y
        return puntos
    
    def rotar(self,puntos,pivote,angulo):
        # Generando matriz para la rotación
        radianes = math.radians(angulo)
        rotacion = [[math.cos(radianes), -math.sin(radianes)] , [math.sin(radianes), math.cos(radianes)]]
        # Traslandando punto pivote al origen y los demás puntos
        puntos = self.trasladar(puntos,(-pivote[0]),(-pivote[1]))
        # Rotando puntos
        for i in range(len(puntos)):
            p_temp = [puntos[i][0],puntos[i][1]]   # Almacenando el punto para poder manipularlo después
            p_temp[0] = (rotacion[0][0]*puntos[i][0])+(rotacion[0][1]*puntos[i][1])  # Rotacion de x
            p_temp[1] = (rotacion[1][0]*puntos[i][0])+(rotacion[1][1]*puntos[i][1])  # Rotacion de y
            puntos[i][0], puntos[i][1] = p_temp[0], p_temp[1]  # Asignando los nuevos valores de x y y
        # Trasladando punto pivote y los demás puntos a la posición original
        puntos = self.trasladar(puntos,pivote[0],pivote[1])
        return puntos

    def get_puntos(self):
        return self.puntos            

           
class Transf_3D:
    def __init__(self,puntos,tipo):
        self.puntos = puntos
        # Aplicando el tipo de transformacion
        if(tipo == "ROTAR"):
            eje_rotacion = input("Ingresa el eje de la rotación (x, y o z): ").upper()    
            angulo = float(input("Ingresa el ángulo (Solo el valor númerico): "))
            self.puntos = self.rotar(puntos,eje_rotacion,angulo)     
        elif(tipo == "TRASLADAR"):
            tras_x = float(input("Ingresa el valor de la traslación en x: ")) 
            tras_y = float(input("Ingresa el valor de la traslación en y: ")) 
            tras_z = float(input("Ingresa el valor de la traslación en z: ")) 
            self.puntos = self.trasladar(puntos,tras_x,tras_y,tras_z)
        elif(tipo == "ESCALAR"):
            esca = float(input("Ingresa el valor del escalamiento en decimales: "))
            self.puntos = self.escalar(puntos,esca)
        
    def trasladar(self,puntos,tras_x,tras_y,tras_z):
        # Obteniendo los vertices para manipular los puntos
        vertices = list(puntos.keys()) 
        # Aplicando transformación
        for v in vertices:
            puntos[v][1][0] = puntos[v][1][0]+(tras_x) # punto x
            puntos[v][1][1] = puntos[v][1][1]+(tras_y)  # punto y
            puntos[v][1][2] = puntos[v][1][2]+(tras_z)  # punto z
        return puntos
    
    def escalar(self,puntos,esca):
        # Obteniendo los vertices del grafo para manipular los puntos 
        vertices = list(puntos.keys()) 
        # Obteniendo primer punto para usarlo como pivote
        tras_x, tras_y, tras_z = puntos[vertices[0]][1][0],puntos[vertices[0]][1][1],puntos[vertices[0]][1][2] 
        # Trasladando figura al origen utilizando el primer punto como punto pivote
        puntos = self.trasladar(puntos, (-tras_x), (-tras_y), (-tras_z))
        # Aplicando escalación
        for v in vertices:
            puntos[v][1][0] = puntos[v][1][0]*esca # punto x
            puntos[v][1][1] = puntos[v][1][1]*esca  # punto y
            puntos[v][1][2] = puntos[v][1][2]*esca  # punto z
        # Regresando puntos a la posición original
        puntos = self.trasladar(puntos, tras_x, tras_y, tras_z)
        return puntos
    
    def rotar(self,puntos,eje_rotacion,angulo):
        # Obteniendo los vertices del grafo para manipular los puntos 
        vertices = list(puntos.keys()) 
        # Generando radianes para la rotación
        radianes = math.radians(angulo)

        # Trasladando un vértice de la figura al origen para comenzar a poner en paralelo uno de los ejes
        tras_x, tras_y, tras_z = puntos[vertices[0]][1][0],puntos[vertices[0]][1][1],puntos[vertices[0]][1][2]  # x,y,z
        puntos = self.trasladar(puntos, (-tras_x), (-tras_y), (-tras_z))

        # Trasladando otro punto para colocarlo sobre el eje de rotación elegido (el punto en el origen no se mueve)
        punto_origen = [puntos[vertices[0]][1][0],puntos[vertices[0]][1][1],puntos[vertices[0]][1][2]]  # [x,y,z]  No se mueve
        if(eje_rotacion == "X"):
            paralelo_x, paralelo_y, paralelo_z = puntos[vertices[1]][1][0], 0, 0  # x,y,z  
            puntos = self.trasladar(puntos, (-paralelo_x), (paralelo_y), (paralelo_z))  #Solo se mueve el eje elegido
        elif(eje_rotacion == "Y"):
            paralelo_x, paralelo_y, paralelo_z = 0, puntos[vertices[1]][1][0], 0  # x,y,z
            puntos = self.trasladar(puntos, (paralelo_x), (-paralelo_y), (paralelo_z))  #Solo se mueve el eje elegido
        elif(eje_rotacion == "Z"):
            paralelo_x, paralelo_y, paralelo_z = 0, 0, puntos[vertices[1]][1][0]  # x,y,z
            puntos = self.trasladar(puntos, (paralelo_x), (paralelo_y), (-paralelo_z))  #Solo se mueve el eje elegido
        puntos[vertices[0]][1] = punto_origen  # Reacomodando punto origen 
        
        # Aplicando rotación
        if(eje_rotacion == "Z"):
            for v in vertices:
                p_tmp = [0,0,0]  # Lista para almacenar el punto actual para poder asignarlo después
                p_tmp[0] = (puntos[v][1][0]*(math.cos(radianes))) - (puntos[v][1][1]*(math.sin(radianes))) # Rotacion x
                p_tmp[1] = (puntos[v][1][0]*(math.sin(radianes))) + (puntos[v][1][1]*(math.cos(radianes))) # Rotacion y
                p_tmp[2] = puntos[v][1][2] # Rotacion z
                puntos[v][1] = p_tmp
        elif(eje_rotacion == "X"):
            for v in vertices:
                p_tmp = [0,0,0]  # Lista para almacenar el punto actual para poder asignarlo después
                p_tmp[0] = puntos[v][1][0] # Rotacion x
                p_tmp[1] = (puntos[v][1][1]*(math.cos(radianes))) - (puntos[v][1][2]*(math.sin(radianes))) # Rotacion y
                p_tmp[2] = (puntos[v][1][1]*(math.sin(radianes))) + (puntos[v][1][2]*(math.cos(radianes))) # Rotacion z
                puntos[v][1] = p_tmp
        elif(eje_rotacion == "Y"):
            for v in vertices:
                p_tmp = [0,0,0]  # Lista para almacenar el punto actual para poder asignarlo después
                p_tmp[0] = (puntos[v][1][2]*(math.sin(radianes))) + (puntos[v][1][0]*(math.cos(radianes))) # Rotacion x
                p_tmp[1] = puntos[v][1][1] # Rotacion y
                p_tmp[2] = (puntos[v][1][2]*(math.cos(radianes))) - (puntos[v][1][0]*(math.sin(radianes))) # Rotacion z
                puntos[v][1] = p_tmp

        # Regresando el eje paralelo a su posición original
        puntos = self.trasladar(puntos, (paralelo_x), (paralelo_y), (paralelo_z)) 
        puntos[vertices[0]][1] = punto_origen  # Reacomodando punto origen

        # Regresando puntos a su posición original respecto al origen
        puntos = self.trasladar(puntos, (tras_x), (tras_y), (tras_z))

        return puntos

    def get_puntos(self):
        return self.puntos  
        
    
# Mostrar puntos     
def tabla_puntos(puntos):
    if(type(puntos) == list):  # Mostrar puntos si es figura 2D
        for i in range(len(puntos)):
            print(f"(x{i+1},y{i+1}) --> ({round(puntos[i][0], 4)},{round(puntos[i][1], 4)})")
    else:  # Mostrar puntos si es figura 3D
        vertices = list(puntos.keys())
        print(f"  --> (x, y, z)")
        for v in vertices:
            print(f"{v} --> {round(puntos[v][1][0], 4), round(puntos[v][1][1], 4), round(puntos[v][1][2], 4)}")

        
def graficar2D(puntos):
    x,y = [],[]
    # Separando puntos de x y y para graficarlos
    for p in puntos:
        x.append(p[0])
        y.append(p[1])
    # Cerrando figura con el primer punto
    x.append(puntos[0][0])
    y.append(puntos[0][1])
    # Graficando
    fig,ax = plt.subplots()
    ax.plot(x,y,color="red")
    ax.set_aspect("equal")
    ax.set_title("Figura después de la transformación",loc="center",
                 fontdict={"fontsize":11, "fontweight":"bold"})
    plt.show()

def graficar3D(puntos):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    vertices = list(puntos.keys()) # Obtiendo vertices para recorrer el grafo

    # INICIANDO RECORRIDO PARA GRAFICACIÓN
    cone_hechas = []  # Lista para registrar las conexiónes hechas
    for v in vertices:
        conexiones = puntos[v][0]  # Obteniendo conexiones
        puntos_vertice = puntos[v][1]  # Obteniendo los puntos del vértice actual   
        for c in conexiones:
            # Verificando si ya se realizó la conexión
            if((v+c) in cone_hechas) or ((c+v) in cone_hechas):
                pass
            else: # Realizando conexiones
                punto_conexion = puntos[c][1] # Obteniendo puntos del punto con el que se conecta

                x = np.array([[puntos_vertice[0],punto_conexion[0]]])  # Obtiendo las conexiones en x para la linea
                y = np.array([[puntos_vertice[1],punto_conexion[1]]])  # Obtiendo las conexiones en y para la linea
                z = np.array([[puntos_vertice[2],punto_conexion[2]]])  # Obtiendo las conexiones en z para la linea

                # Graficando linea
                ax.plot_wireframe(x,y,z)
                # Registrando linea en el historial
                cone_hechas.append(c+v)

                # Creando un plano para representar la figura con los ejes equitativamente porque matplotlib no lo soporta por defecto
                max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max()
                Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(x.max()+x.min())
                Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(y.max()+y.min())
                Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(z.max()+z.min())
                # Aplicando plano
                for xb, yb, zb in zip(Xb, Yb, Zb):
                    ax.plot([xb], [yb], [zb], 'w')
    plt.show()
    
# Define que transformación se hace y muestra los resultados
def transformaciones(dimension,tipo,puntos=None): 
    if(dimension == "2D"):
        # Verificando si ya se tienen puntos para la figura
        if(puntos == None):
            # Pidiendo los puntos en orden
            n_puntos = int(input("¿Cuántos puntos tiene la figura?: "))
            puntos = [[0.0 for i in range(2)] for j in range(n_puntos)] # Generando espacio de los puntos
            
            print("Introduzca los valores de los puntos en x,y siguiendo el sentido de las manecillas del reloj.")
            for i in range(n_puntos):
                puntos[i][0] = float(input(f"Punto x{i+1}: "))  # x
                puntos[i][1] = float(input(f"Punto y{i+1}: "))  # y
            transf = Transf_2D(puntos, tipo)  # Creando transformacion
            puntos = transf.get_puntos()
            graficar2D(puntos) # Graficando
        else:
            transf = Transf_2D(puntos, tipo) 
            puntos = transf.get_puntos()
            graficar2D(puntos) # Graficando
                   
    elif(dimension == "3D"):
        # Verificando si ya se tienen puntos para la figura
        if(puntos == None):
            puntos = {}  # Grafo para guardar la información de los puntos 
            # Pidiendo los puntos 
            n_puntos = int(input("¿Cuántos puntos tiene la figura?: "))
            print("Antes de ingresar los puntos, asegurate de asignarle a cada punto una letra (A, B, C, etc.)")
            
            for i in range(n_puntos):
                letra = input("Indica la letra del punto que se quiere ingresar: ").upper()
                conexiones = input(f"Ingresa las letras de los puntos con los que tiene conexión el punto {letra} separandolos únicamente con comas: ").upper()
                conexiones = conexiones.split(sep=",")  # Separando los puntos con los que tiene conexión para tenerlos en una lista
                x = float(input(f"Ingresa el valor de x del punto {letra}: "))  # valor de x
                y = float(input(f"Ingresa el valor de y del punto {letra}: "))  # valor de y
                z = float(input(f"Ingresa el valor de z del punto {letra}: "))  # valor de z

                # Guardando puntos en el grafo
                puntos[letra] = [conexiones,[x,y,z]]
            transf = Transf_3D(puntos, tipo)  # Creando transformación
            puntos = transf.get_puntos()
            graficar3D(puntos) # Graficando
        else: 
            transf = Transf_3D(puntos, tipo) 
            puntos = transf.get_puntos()
            graficar3D(puntos) # Graficando
         

    # Mostrando resultados
    print("\n- Puntos después de la transformación -")
    tabla_puntos(puntos) 
    return puntos  # Devuelve los puntos para que se pueden utilizar nuevamente
        

if __name__ == "__main__":    
    terminar = False
    nueva_trans = True
    while(not terminar):
        # Verificando si es nueva transformación
        if(nueva_trans==True):
            dimension = (input("Selecciona la dimensión (2D o 3D): ")).upper()
            tipo = (input("Selecciona la transformación (rotar, trasladar o escalar): ")).upper()
            puntos = transformaciones(dimension, tipo)
        else:
            tipo = (input("Selecciona la transformación (rotar, trasladar o escalar): ")).upper()
            puntos = transformaciones(dimension, tipo, puntos)

        aux = input("¿Deseas hacer otra transformación? (Si o No): ").upper()
        if(aux=="NO"):
            terminar = True
        elif(aux=="SI"):
            aux = (input("¿Utilizar los puntos generados por la transformación anterior? (Si o No): ")).upper()
            if(aux=="SI"):
                nueva_trans = False
            elif(aux=="NO"):
                nueva_trans = True