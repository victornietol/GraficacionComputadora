# FRACTALES

import numpy as np
import matplotlib.pyplot as plt
import random
from numpy.random import random as rn


# Seleccionar color del fractal
class ColorFractal:
    def __init__(self):
        self.colores = ["autumn","bone","cool","copper","flag","gray","hot","hsv","infierno","jet","pink","prism",\
                        "viridis","winter"]
    def color_set(self):
        aux = int(input("¿Quieres un color aleatorio o prefieres seleccionar uno:\n   1. Aleatorio\n   2. Seleccionar\n\nOpción: "))
        if(aux==1):
            return random.choice(self.colores)
        elif(aux==2):
            print("Los colores son: ",end="")
            for c in self.colores:
                print(c,end=",")
            return input("\nColor: ")


# Fractal Mandelbrot
class Mandelbrot:
    def __init__(self):
        # Parámetros del fractal
        xmin, xmax, xn = -2.0, 1.0, 1000
        ymin, ymax, yn = -1.5, 1.5, 1000
        max_iter = 100
        color = ColorFractal() # Asignando color

        # Genera el fractal
        mandelbrot = self.mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, max_iter)

        # Visualiza el fractal
        plt.imshow(mandelbrot.T, cmap=color.color_set())
        plt.axis('off')
        plt.show()

    # Función que generará el fractal
    def mandelbrot_set(self,xmin, xmax, ymin, ymax, xn, yn, max_iter):
        x, y = np.meshgrid(np.linspace(xmin, xmax, xn), np.linspace(ymin, ymax, yn))
        c = x + y*1j
        z = c
        div_time = max_iter + np.zeros(z.shape, dtype=int)
        for i in range(max_iter):
            z = z**2 + c
            diverge = z*np.conj(z) > 2**2
            div_now = diverge & (div_time==max_iter)
            div_time[div_now] = i
            z[diverge] = 2
        return div_time   


# Fractal Julia
class Julia:
    def __init__(self):
        # Define los parámetros del fractal
        xmin, xmax, xn = -1.5, 1.5, 1000
        ymin, ymax, yn = -1.5, 1.5, 1000
        max_iter = 80
        c = complex(0.285, 0.01)
        color = ColorFractal() # Asignando color

        # Genera el fractal
        julia = self.julia_set(xmin, xmax, ymin, ymax, xn, yn, c, max_iter)

        # Visualiza el fractal
        plt.imshow(julia.T, cmap=color.color_set())
        plt.axis('off')
        plt.show()

    def julia_set(self,xmin, xmax, ymin, ymax, xn, yn, c, max_iter):
        x, y = np.meshgrid(np.linspace(xmin, xmax, xn), np.linspace(ymin, ymax, yn))
        z = x + y*1j
        div_time = max_iter + np.zeros(z.shape, dtype=int)
        for i in range(max_iter):
            z = z**2 + c
            diverge = z*np.conj(z) > 2**2
            div_now = diverge & (div_time==max_iter)
            div_time[div_now] = i
            z[diverge] = 2
        return div_time
 
# Fractal Helecho    
class Helecho:
    def __init__(self):
        # Genera el helecho de Barnsley
        x, y = self.barnsley_fern(100000)
        
        # Visualiza el helecho de Barnsley
        color = self.color_set()
        plt.scatter(x, y, s=0.2, c=color)
        plt.axis('off')
        plt.show()  
        
    # Asignación de color
    def color_set(self):
        colores = ["red","green","blue","cyan","magenta","black"]
        aux = int(input("¿Quieres un color aleatorio o prefieres seleccionar uno:\n   1. Aleatorio\n   2. Seleccionar\n\nOpción: "))
        if(aux==1):
            return random.choice(colores)
        elif(aux==2):
            print("\nLos colores son: ",end="")
            for c in colores:
                print(c,end=",")
            return input("\nColor: ")
    
    # Define las funciones de transformación afín
    def f1(self,x, y):
        return 0, 0.16*y    
    def f2(self,x, y):
        return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6  
    def f3(self,x, y):
        return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6    
    def f4(self,x, y):
        return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44    
    
    # Define la función que genera el helecho de Barnsley
    def barnsley_fern(self,n):
        x, y = 0, 0
        xlist, ylist = [], []
        for i in range(n):
            rand = random.uniform(0, 1)
            if rand < 0.01:
                x, y = self.f1(x, y)
            elif rand < 0.86:
                x, y = self.f2(x, y)
            elif rand < 0.93:
                x, y = self.f3(x, y)
            else:
                x, y = self.f4(x, y)
            xlist.append(x)
            ylist.append(y)
        return xlist, ylist    


# Fractal Triángulo de Sierpinsky        
class Sierpinsky:
    def __init__(self):
        n_iter = 10000
        medioX, medioY = 0,0
        
        # Punto inicial
        pX, pY = 0.5,0.5
        
        # Coordendas de los puntos medios
        coordsX = [pX]
        coordsY = [pY]
        
        # Puntos de los vértices del primer triángulo
        inicialX = [0,0.5,1]
        inicialY = [0,np.sqrt(3)/2,0]
        
        # Creación de punto aleatorios entre 0 y 1 para evaluación de vértices
        n_random = []
        n_random = rn(n_iter)
        
        # Creando fractal
        x,y = self.sierpinsky_set(n_iter,medioX,medioY,pX,pY,coordsX,coordsY,inicialX,inicialY,n_random)
        color = self.color_set()
        plt.plot(coordsX,coordsY,color+" ,")
        plt.axis('off')
        plt.show()
        
    # Asignación de color
    def color_set(self):
        colores = ["r","g","b","c","m","k"]
        aux = int(input("¿Quieres un color aleatorio o prefieres seleccionar uno:\n   1. Aleatorio\n   2. Seleccionar\n\nOpción: "))
        if(aux==1):
            return random.choice(colores)
        elif(aux==2):
            print("Los colores son: ",end="")
            for c in colores:
                print(c,end=",")
            return input("\nColor: ")
   
    # Proceso para crear el fractal    
    def sierpinsky_set(self,n_iter,medioX,medioY,pX,pY,coordsX,coordsY,inicialX,inicialY,n_random):
        for i in range(n_iter):
            
            # Eligiendo vertice al azar
            if(n_random[i] < 1/3):
                verticeX = inicialX[0]
                verticeY = inicialY[0]
            elif(1/3 < n_random[i] < 2/3):
                verticeX = inicialX[1]
                verticeY = inicialY[1]
            elif(2/3 < n_random[i]):
                verticeX = inicialX[2]
                verticeY = inicialY[2]
            
            # Generando puntos medios
            if(i==0):   # Si es la primera iteración
                medioX = (verticeX + pX)/2
                medioY = (verticeY + pY)/2
            else:   # Después de la primera iteración
                medioX = (verticeX + medioX)/2
                medioY = (verticeY + medioY)/2
            
            # Guardando puntos medios generados
            coordsX.append(medioX)
            coordsY.append(medioY)
        return coordsX, coordsY
    
    
# Fractal Mandelbrot modificado
class Modificado:
    def __init__(self):
        # Parámetros del fractal
        xmin, xmax, xn = -2.0, 1.0, 1000
        ymin, ymax, yn = -1.5, 1.5, 1000
        max_iter = 100
        color = ColorFractal() # Asignando color

        # Genera el fractal
        mandelbrot = self.mandelbrotM_set(xmin, xmax, ymin, ymax, xn, yn, max_iter)

        # Visualiza el fractal
        plt.imshow(mandelbrot.T, cmap=color.color_set())
        plt.axis('off')
        plt.show()

    # Función que generará el fractal
    def mandelbrotM_set(self,xmin, xmax, ymin, ymax, xn, yn, max_iter):
        x, y = np.meshgrid(np.linspace(xmin, xmax, xn), np.linspace(ymin, ymax, yn))
        c = x + y*1j
        z = c
        div_time = max_iter + np.zeros(z.shape, dtype=int)
        for i in range(max_iter):
            z = z**z*2 + c-z
            diverge = z*np.conj(z) > 2**3
            div_now = diverge & (div_time==max_iter)
            div_time[div_now] = i
            z[diverge] = 2
        return div_time    
        

        
# Menú programa
def iniciar():
    terminar = False
    while(terminar!=True):
        print("¿Qué fractal deseas visualizar?:")
        print("   1. Mandelbrot\n   2. Julia\n   3. Helecho\n   4. Triángulo de Sierpinsky\n"
              +"   5. Mandelbrot modificado\n   6. Salir")
        opcFractal = int(input("Opción: "))

        # Mandelbrot
        if(opcFractal==1):
            Mandelbrot()
            print()

        # Julia
        elif(opcFractal==2):
            Julia()
            print()
            
        # Helecho
        elif(opcFractal==3):
            Helecho()
            print()
        
        # Triángulo de Sierpinsky
        elif(opcFractal==4):
            Sierpinsky()
            print()
            
        # Fractal basado en el Fractal Mandelbrot
        elif(opcFractal==5):
            Modificado()
            print()

        elif(opcFractal==6):
            print("\nPrograma finalizado.")
            break   

iniciar()