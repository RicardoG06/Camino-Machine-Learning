objetivo = int(input('Escoge un numero: '))

epsilon = 0.01  # Definimos nuestro margen de error.

bajo = 0.0      # Inicializamos la parte baja de nuestra busqueda como 0
alto = max(1.0, objetivo)   # Entre el numero que ingresamos y 1 vamos a tomar el mayor valor.
respuesta = (alto + bajo) / 2   # Definimos la mitad entre bajo y alto.

# Mientras el margen de error sea mayor a epsilon.
while abs(respuesta**2 - objetivo) >= epsilon:

    # Si ((alto+bajo)/2)^2 es menor a nuestro numero objetivo
    if respuesta**2 < objetivo:
        
        # Definimos la parte baja de nuestra busqueda como (alto + bajo)/2
        bajo = respuesta

    # En caso que (alto+bajo)/2 es mayor a nuestro numero objetivo
    else: 
        # Definimos la parte baja de nuestra busqueda como (alto + bajo)/2
        alto = respuesta

    # Luego definimos nuevamente la mitad entre alto y bajo.
    respuesta = (alto + bajo) / 2

# Cuando el ciclo ya alcance un error menor a epsilon imprimiremos el resultado.
print(f'La raiz cuadrada de {objetivo} es {respuesta}')