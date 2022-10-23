# Importacion de la biblioteca para el entorno grafico.
from struct import pack
import tkinter

# Crear una ventana o contenedor para los elementos graficos.
ventana = tkinter.Tk()

# Configuraciones de la ventana.
ventana.geometry("500x500") # Tamaño de la ventana.

# --------Agregar elementos graficos---------
#Agregar una etiqueta con parametros (¿Donde se ubicara, texto a desplegar?)
etiqueta = tkinter.Label(ventana, text = "Hola Mundo", bg = "blue")
# etiqueta.pack() # Ponerlo en ventana (sin especificar donde ponerlo).
# etiqueta.pack(side = tkinter.BOTTOM)
etiqueta.pack(fill = tkinter.Y, expand = True) # Estirar el texto (tkinter.BOTH -> Sirve para expandirlo en el eje X y Y).

# Declarar funciones para los botones.
def saludo(nombre):
    print("Hola" + nombre)

# Hacer botones.
boton1 = tkinter.Button(ventana, text = "Preciona", padx = 40, pady = 50, command = lambda: saludo("Python")) # Llamar la funcion command y el metodo sin parentesis. Utilizar lambda para pasar parametros o mensajes.
boton1.pack()

# Cajas de Texto.
cajaTexto = tkinter.Entry(ventana, font = "Helvetica 50")
cajaTexto.pack()

# Desplegar el Texto en una etiqueta de la caja de Texto.
etiqueta2 = tkinter.Label(ventana)
etiqueta2.pack()

# Funcion para tomar lo de la caja de Texto.
def textoDeLaCaja():
    texto20 = cajaTexto.get() # El get obtiene lo que tiene nuestra caja de texto.
    etiqueta2["text"] = texto20 # Aqui desplegamos lo que se escribio en la ventana.

# Obtener el Texto de la caja de Texto del usuario.
boton2 = tkinter.Button(ventana, text = "click", command = textoDeLaCaja)
boton2.pack()

# Creamos un mainloop, para llevar el registro de lo que sucede en nuestra ventana.
ventana.mainloop() # Este seimpre va.
