import random
import math

def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)
    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2
    return acumulador / len(X)

def desviacionEstandar(X):
    return math.sqrt(varianza(X))

if __name__ == '__main__':
    X = [random.randint(1,21) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacionEstandar(X)

    print(f'Arreglo X: {X}')
    print(f'Media: {mu}')
    print(f'Varianza: {Var}')
    print(f'Desviacion estandar: {sigma}')

#Alternativas rapidas:

'''import random
import statistics

if __name__ == '__main__':

    edades = [random.randint(1,35) for i in range (20)]
    print(edades)
    print(statistics.mean(edades))'''

'''
import numpy
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

'''