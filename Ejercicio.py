# Posicionar elementos en la ventana.
import tkinter

# Declaracion de Nuestra Ventana.
ventana =  tkinter.Tk()
ventana.geometry("400x300")

# Metodo Grid.
boton1 = tkinter.Button(ventana, text = "boton1", width = 10, height = 5)
boton2 = tkinter.Button(ventana, text = "boton2", width = 10, height = 5)
boton3 = tkinter.Button(ventana, text = "boton3", width = 10, height = 5)

boton1.grid(row = 0, column = 0)
boton2.grid(row = 1, column = 1)
boton3.grid(row = 2, column = 2)

# Creamos un mainloop, para llevar el registro de lo que sucede en nuestra ventana.
ventana.mainloop() # Este seimpre va.