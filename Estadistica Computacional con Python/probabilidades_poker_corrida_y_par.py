import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    
    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        #Metodo para encontrar una corrida dentro de una mano
        valores = list(map(int, valores))
        valores = sorted(valores)
        print(valores)
        i = 1
        tam_valores = len(valores)

        for val in valores:
            if i < tam_valores:
                if val + 1 == valores[i]:
                    cond = True
                else:
                    cond = False
                    break
                i += 1
                print(cond)
        if cond == True:
            pares +=1

        #Metodo para encontrar un par en una cantidad determinada de manos    
        '''counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 3:
                pares += 1
                break'''

    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener una corrida en una mano de {tamano_mano} barajas es {probabilidad_par}')


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)