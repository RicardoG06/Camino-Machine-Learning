import os
import random as random
import math as math
import statistics as std
from bokeh.plotting import figure, output_file, show
os.system('cls')

intentos = 10
numero_de_agujas = 100

def estimar_pi(numero_de_agujas):
    dentro_circulo_x = []
    dentro_circulo_y = []
    fuera_circle_x = []
    fuera_circle_y = []
    pi_array =[]

    for i in range(numero_de_agujas):
        pos_x = random.uniform(-1,1)
        pos_y = random.uniform(-1,1)

        if math.sqrt(pos_x**2 + pos_y**2) <= 1:
            dentro_circulo_x.append(pos_x)
            dentro_circulo_y.append(pos_y)
        else:
            fuera_circle_x.append(pos_x)
            fuera_circle_y.append(pos_y)

    estimacion_pi = (4 * len(dentro_circulo_x)) / numero_de_agujas
    return (estimacion_pi, dentro_circulo_x, dentro_circulo_y, fuera_circle_x, fuera_circle_y)
    #return ()

def crear_muestra(intentos):
    arreglo_pi =[]
    for i in range(intentos):
        pivalor,dentro_circulo_x, dentro_circulo_y, fuera_circle_x, fuera_circle_y = estimar_pi(numero_de_agujas)
        arreglo_pi.append(pivalor)
    return (arreglo_pi, dentro_circulo_x, dentro_circulo_y, fuera_circle_x, fuera_circle_y)

Desviacion = 1       # Valor inicial para poder empezar el ciclo while
presicion = 0.1     # Precision en cifras significativas para determinar el 
                    # valor estimado de pi (CUIDADO!!!!)

iteraciones = 1

while Desviacion >= (presicion / 1.96):
    arreglo_pi, dentro_circulo_x, dentro_circulo_y, fuera_circle_x, fuera_circle_y = crear_muestra(intentos)
    Desviacion = std.stdev(arreglo_pi)
    varianza = std.variance(arreglo_pi) 
    media = std.mean(arreglo_pi)
    
    print(f'------------------       Numero de Iteraciones: {(iteraciones)}      ------------------')
    print(f'Desviacion Estandar: {round(Desviacion,5)}, Varianza: {round(varianza,5)}, estimacion de pi: {round(media,5)}')
    print(f'Numero de intentos: {intentos}, Numero de agujas: {numero_de_agujas}\n\n')
    #print(f)
    numero_de_agujas *= 10
    intentos *= 10
    iteraciones += 1

output_file("Grafico de estimacion de pi.html")
plot = figure(plot_width=600, plot_height=600)
plot.circle(dentro_circulo_x, dentro_circulo_y, size=5, color="red", alpha=0.5)
plot.circle(fuera_circle_x, fuera_circle_y, size=5, color="navy", alpha=0.5)
show(plot)