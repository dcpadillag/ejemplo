import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sys #system library
import os #libreria para navegar en consola
from matplotlib import rc


#a = sys.argv[1] #sys.argv es una lista de argumentos que pasa a python3

#print(a)

# longitud = sys.argv[1:] #asigna a la variabloe longitud el argumento 1 de python
# name = 'I1_L_'+longitud+'nm_M1.txt' # creando un nombre estandar usando la variable
# longitud
# print(name)

# Los datos de entrada son los 5 archivos tomados para las 5 longitudes de onda y
# y la repeticion de la medida que se va a tener en cuenta

# el dato de salida es la grafica de la corriente y el voltaje

# n = int(input('ingrese la repeticion que se utilizara:' ))

# V = np.zeros(len(data[:,1]))


def grafica(longitud, n):
    os.chdir('datos/')
    V = []
    I = []
    for L in longitud:
        data = np.loadtxt('Ifijo_L_'+L+'nm_M'+n+'.txt', dtype = 'float')
        V.append(data[:,1]) #segunda columna de data
        I.append(data[:,2]) #tercera columna de data
    os.chdir('..')
    return V, I

longitud = sys.argv[2:]
n = sys.argv[1]
V, I = grafica(longitud, n)
 
######PARAMETROS PARA PLOT#####
rc('font', **{'serif': ['Computer Modern']})
rc('text', usetex=True)
rc('legend', fontsize=15)
rc('xtick', labelsize=20)
rc('ytick', labelsize=20)
##############################
plt.figure(figsize = (10,9))

colors=['r','midnightblue','g','c','m']
markers=['o','s','D','^','v']
for j in range(len(V)):
    plt.plot(V[j],I[j],color=colors[j],marker=markers[j])

plt.legend([r"$\lambda=365$ $nm$",'405 nm','436 nm','546 nm','578 nm'])
plt.title('Caracteristica corriente voltaje para el conjunto de medidas '+str(n),fontsize=20) 
plt.grid()
plt.show()



A*EXP(B*X)+C