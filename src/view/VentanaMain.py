
from tkinter import *
from VentanaCompra import VentanaCompra
from VentanaCliente import VentanaCliente
from view.VentanaProducto import VentanaProducto
from view.VentanaTrabajador import VentanaTrabajador

def set_ventana1():
    VentanaCliente(root)

def set_ventana2():
    VentanaCompra(root)

def set_ventana3():
    VentanaTrabajador(root)

def set_ventana4():
    VentanaProducto(root)
    


    


if __name__ == '__main__':
    root =  Tk()
    root.title('Ventana Principal')
    canvas = Canvas(root,height=900,width=900)
    canvas.pack()


    frame = Frame()
    frame.place(relx=0.1,rely=0.1,relwidth=0.9,relheight=0.8,width=500)


    button = Button(frame,text='VentanaCliente',command=lambda: set_ventana1())
    button.grid(row=1,column=1,sticky=W+E)
    button = Button(frame,text='VentanaCompra',command=lambda: set_ventana2())
    button.grid(row=1,column=2,sticky=W+E)
    button = Button(frame,text='VentanaTrabajador',command=lambda: set_ventana3())
    button.grid(row=1,column=3,sticky=W+E)
    button = Button(frame,text='VentanaProducto',command=lambda: set_ventana4())
    button.grid(row=1,column=4,sticky=W+E)
    root.mainloop()