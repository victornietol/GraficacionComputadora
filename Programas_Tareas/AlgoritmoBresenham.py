# Algoritmo Brensenham

import matplotlib.pyplot as plt

# Coordenadas
x0,y0 = 5,5 
x1,y1 = 30,20

# Punteros y lista de puntos
pointX,pointY = x0,y0
points = [(x0,y0)]
pk_memory = []  #OPCIONAL

# Valores 
deltaY = y1 - y0
deltaX = x1 - x0
dosDeltaY = deltaY*2

# Procesos
pk = 2*deltaY - deltaX
pk_memory.append(pk) #OPCIONAL

while(pointX != x1 and pointY != y1):
    if(pk < 0):
        pointX+=1
        points.append((pointX,pointY))
        pk = pk+ 2*deltaY
        pk_memory.append(pk) #OPCIONAL
    elif(pk > 0):
        pointX+=1
        pointY+=1
        points.append((pointX,pointY))
        pk = pk + 2*deltaY - 2*deltaX
        pk_memory.append(pk) #OPCIONAL
    else:
        print("Igual que cero")

aux=0
for cord in points:
    #Imprimir con valores pk
    #print(pk_memory[aux],"|",cord)
    #aux+=1
    print(cord)
    
#print(x0,y0)

# Graficando
verticesX, verticesY = [], []

for vertices in points:
    verticesX.append(vertices[0])
    verticesY.append(vertices[1])

plt.plot(verticesX, verticesY,"r")
plt.show()    





# VERSION DESCENDENTE
import matplotlib.pyplot as plt

# Coordenadas
x0,y0 = 25,25 
x1,y1 = 40,5

# Punteros y lista de puntos
pointX,pointY = x0,y0
points = [(x0,y0)]
pk_memory = []  #OPCIONAL

# Valores 
deltaY = abs(y1 - y0)
deltaX = abs(x1 - x0)
dosDeltaY = deltaY*2

# Procesos
pk = (2*deltaY) - (deltaX)
pk_memory.append(pk) #OPCIONAL

for i in range(deltaY):
    if(pk < 0):
        pointY-=1
        points.append((pointX,pointY))
        pk += 2*deltaX
        pk_memory.append(pk) #OPCIONAL
    elif(pk > 0):
        pointX+=1
        pointY-=1
        points.append((pointX,pointY))
        pk += (2*deltaX) - (2*deltaY)
        pk_memory.append(pk) #OPCIONAL
    else:
        print("Igual que cero")

aux=0
for cord in points:
    #Imprimir con valores pk
    #print(pk_memory[aux],"|",cord)
    #aux+=1
    print(cord)
    
#print(x0,y0)

# Graficando
verticesX, verticesY = [], []

for vertices in points:
    verticesX.append(vertices[0])
    verticesY.append(vertices[1])

plt.plot(verticesX, verticesY,"r")
plt.show()    

#plt.plot(args, kwargs)


# Linea descendente (Ivan)
def bresenham(tuple1,tuple2):
  difx = abs(tuple2[0] - tuple1[0])
  dify = abs(tuple2[1] - tuple1[1])
  p0 = (2*dify)-(difx)
  res = [tuple1[0],tuple1[1]]
  incremMenor0 = 2 * difx
  incremMayor0 = (2*difx)-(2*dify)
  print(f"(x,y) = ({res[0]},{res[1]})")
  for ciclo in range(dify):
    if p0 < 0:
          res[1] -= 1
          print(f"p_k = {p0} // (x,y) = ({res[0]},{res[1]})")
          p0 += incremMenor0
    else:
          res[0] += 1
          res[1] -= 1
          print(f"p_k = {p0} // (x,y) = ({res[0]},{res[1]})")
          p0 += incremMayor0
bresenham((25,25), (40,5))


