import numpy as np
import matplotlib.pyplot as plt

class TrianguloS:
    def __init__(self):
        inicialesX = [0,1,2]
        inicialesY = [0,(np.sqrt(3)*2)/2,0]
        cierreInicial = [0,0,0]
        n_iter = 10
        
        self.triangulo_set(inicialesX, inicialesY, cierreInicial,n_iter)
        
    def get_puntoMedio(self,x1,x2,y1,y2):
        x = (x1+x2)/2
        y = (y1+y2)/2
        return x,y
        
    def triangulo_set(self,inicialesX,inicialesY,cierreInicial,n_iter):
        # Generando el triangulo inicial
        plt.fill_between(inicialesX,inicialesY,cierreInicial,color="blue")
        
        # Creando lista de vertices para obtener puntos medios
        verticesX = [[0,1,2]]
        verticesY = [[0,(np.sqrt(3)*2)/2,0]]
        
        # Creando los nuevos triángulos segun el número de iteraciones
        #for i in range(n_iter):   (este sera la base para hacer la repeticion del siguiente proceso)
            
        
        # Obteniendo puntos medios
        x0,y0 = self.get_puntoMedio(verticesX[0][0], verticesX[0][1], verticesY[0][0], verticesY[0][1])
        x1,y1 = self.get_puntoMedio(verticesX[0][1], verticesX[0][2], verticesY[0][1], verticesY[0][2])
        x2,y2 = self.get_puntoMedio(verticesX[0][0], verticesX[0][2], verticesY[0][0], verticesY[0][2])
        pMediosX = [x0,x1,x2,x0]
        pMediosY = [y0,y1,y2,y0]
        
        """
        # Obteniendo punto para el cierre de la figura
        dif = abs(pMediosX[0]-pMediosX[2])/2
        dif += pMediosX[0] 
        cierre = [3,3.4,4]
        """
        # Graficando el nuevo triangulo
        plt.fill_between(pMediosX,pMediosY,color="red")
        
        #plt.plot([x0,x1],[y0,y1],color="yellow")
            
        
            
        """
        for i in range(3):
            verticesX.append(incialesX)
        """
        plt.axis("on")
        
        
        
        
        
        #plt.plot([0,1],[0,1],color="red")
        
        
        
        plt.show()
        
TrianguloS()