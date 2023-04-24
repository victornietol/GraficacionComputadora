import matplotlib.pyplot as plt

def alg_puntoMedioB(r,xc,yc):
    pk = 1-r
    puntos = [[0,r]]
    pActual = [0,r]
    
    while (pActual[0]<pActual[1]):
        if(pk<0):
            pActual[0] += 1
            puntos.append((pActual[0],pActual[1]))
            pk = pk + (2*pActual[0]) +1
        else:
            pActual[0] += 1
            pActual[1] -= 1
            puntos.append((pActual[0],pActual[1]))
            pk = pk + (2*pActual[0]) +1 -(2*pActual[1])
            
    return puntos


def alg_puntoMedioB2(r,xc,yc):
    pk = 1-r
    puntos = [[0,r]]
    pActual = [0,r]
    k = 0
    
    while (pActual[0]<pActual[1]):
        if(pk<0):
            pActual[0] += 1
            dosX = 2*pActual[0]
            dosY = 2*pActual[1]
            puntos.append((pActual[0],pActual[1]))
            
            print(f"{k} | {pk} | {pActual} | {dosX} | {dosY}")
            k += 1            
            
            pk = pk + dosX +1
            

        else:
            pActual[0] += 1
            pActual[1] -= 1
            dosX = 2*pActual[0]
            dosY = 2*pActual[1]
            puntos.append((pActual[0],pActual[1]))
            
            print(f"{k} | {pk} | {pActual} | {dosX} | {dosY}")
            k += 1            
            
            pk = pk + dosX +1 -dosY
            
    return puntos


puntos = alg_puntoMedioB2(55, 0, 0)
x,y = [],[]

for p in puntos:
    x.append(p[0])
    y.append(p[1])
    #print(p)
    
# Completando los cuadrantes

# Cuadrante 1
for p in reversed(puntos):
    x.append(p[1])    
    y.append(p[0])
    #print(f"- | - | ({p[1],p[0]}) | - | -")
    
# Cuadrante 2
for p in puntos:
    x.append(-p[0])
    y.append(p[1])
    #print(f"- | - | {-p[0],p[1]} | - | -")
for p in reversed(puntos):
    x.append(-p[1])    
    y.append(p[0])
    #print(f"- | - | {-p[1],p[0]} | - | -")
    
# Cuadrante 3
for p in puntos:
    x.append(-p[0])
    y.append(-p[1])
    #print(f"- | - | {-p[0],-p[1]} | - | -")
for p in reversed(puntos):
    x.append(-p[1])    
    y.append(-p[0])
    #print(f"- | - | {-p[1],-p[0]} | - | -")
    
# Cuadrante 4
for p in puntos:
    x.append(p[0])
    y.append(-p[1])
    #print(f"- | - | {p[0],-p[1]} | - | -")
for p in reversed(puntos):
    x.append(p[1])    
    y.append(-p[0])
    print(f"- | - | {p[1],-p[0]} | - | -")
  

fig, ax = plt.subplots()
ax.set_aspect("equal")
#plt.figure(figsize=(11,11))
plt.plot(x, y, "s",markersize=3) #markersize=6
plt.grid()
plt.show()