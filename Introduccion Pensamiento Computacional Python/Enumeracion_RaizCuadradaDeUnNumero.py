from time import time

objetivo = int(input('Escoge un entero: '))
respuesta = 0
tiempo_inicial = time()

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:16
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz exacta')

print(f'El programa demoró {time() - tiempo_inicial} segundos ')