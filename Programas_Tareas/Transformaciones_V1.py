import matplotlib.pyplot as plt
import math

# Clase para realizar las transformaciones 2D
class Transf_2D:
    def __init__(self,puntos,tipo):
        self.puntos = puntos
        # Aplicando el tipo de transformacion
        if(tipo == "ROTAR"):
            tmp_piv = int(input("Ingresa el indice del punto correspondiente al punto pivote (Ejemplo: 1 para seleccionar x1,y1): "))
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
        #self.puntos = puntos 
    
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

############################################            
class Transf_3D:
    def __init__(self,puntos,tipo):
        self.puntos = puntos
        print("333DDDD")
    
    
    
    
# Mostrar puntos     
def tabla_puntos(puntos):
    for i in range(len(puntos)):
        print(f"(x{i+1},y{i+1}) --> ({puntos[i][0]},{puntos[i][1]})")
        
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
        transf = Transf_3D(puntos, tipo)  

    # Aqui debo graficar Graficar
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
            #print(puntos)  -----------------> quitar
        else:
            tipo = (input("Selecciona la transformación (rotar, trasladar o escalar): ")).upper()
            puntos = transformaciones(dimension, tipo, puntos)
            #print(puntos) ---------------------> quitar

        aux = input("¿Deseas hacer otra transformación? (Si o No): ").upper()
        if(aux=="NO"):
            terminar = True
        elif(aux=="SI"):
            aux = (input("¿Utilizar los puntos generados por la transformación anterior? (Si o No): ")).upper()
            if(aux=="SI"):
                nueva_trans = False
                #puntos = transformaciones(dimension, tipo, puntos)
            elif(aux=="NO"):
                nueva_trans = True