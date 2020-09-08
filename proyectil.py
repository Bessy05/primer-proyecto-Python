"""
Importante!
Para preparar entorno intalar librerias:
pip install numpy
pip install matplotlib
"""

#Lanzamiento Proyectil 
import numpy as np
import matplotlib.pyplot as plt
#Funciones Fundamentales
#Y(t)
def y_axis(y0,vy0,t,a=-9.8):
    return y0 + (vy0*t) + ((a*(t**2))/2)

#X(t)
def x_axis(x0,v0x0,t):
    return x0 + v0x0*t
#r(t)
def trajectory(x0,y0,vx0,vy0,t):#Utiliza las funciones de posicion para crear pares ordenados
    y = y_axis(y0,vy0,t)
    x = x_axis(x0,vx0,t)
    return (x,y)

#Altura Maxima
def max_height(y,t):#Devuelve la altura maxima que alcanza el proyectil y mapea el tiempo para encontrar el correcto
     maxH= np.amax(y)
     print("La altura maxima se alcanza en  "+str(maxH)+" mts")
     for time,y_element in zip(t,y):
        if y_element==maxH:
            print("en "+ str(time) +"seg")



#Se define el tiempo en un arreglo para evitar asignar cada valor en un tiempo definido
t =np.arange(0,5,0.1)#Crea el arreglo(inicio,Fin,Intervalo)
y =list(map(lambda t:y_axis(5000,30,t),t)) #Realiza un mapeo de el arreglo de tiempo y le aplica la funcion y_axis almacena todos los valores que obtiene y en el tiempo en la lista y
r = list(map(lambda t:trajectory(0,15,2,25,t),t))#Realiza un mapeo de el arreglo de tiempo y le aplica la funcion de trayectoria  cada valor, r obtiene una lista de pares ordenados (x,y)
rx= [x for x,y in r]#Crea una lista con los elementos de x movimiento horizantal
ry= [y for x,y in r]#Crea una lista con los elementos de y movimiento vertical

#Grafico

plt.plot(t,y)
plt.title("Grafico AlturaxTiempo")
plt.xlabel("t seg")
plt.ylabel("h mts")
plt.show()

plt.plot(rx,ry)
plt.title("Grafico AlturaxDistancia")
plt.xlabel("x mts")
plt.ylabel("h mts")
plt.show()

#Altura Maxima
max_height(y,t)






