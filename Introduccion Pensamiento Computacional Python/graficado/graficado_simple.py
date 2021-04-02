from bokeh.plotting import figure, output_file, show
# figure -> ventana donde se grafica
# output_file -> nos permite determinar cual es el nombre del archivo que nosotros generaremos como salida , en este caso lo colocaremos en html 
# show -> genera servidor que se prende y muestra el archivo , en este caso , html , directamente en el browser

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_valores = int(input('Cuantos valores quieres graficar?: '))
    x_valores = list(range(total_valores))
    y_valores =[]

    for x in x_valores:
        val = int(input(f'Valor y para {x}: '))
        y_valores.append(val)
    
    fig.line(x_valores, y_valores, line_width=2)
    show(fig)