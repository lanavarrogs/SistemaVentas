import sys
sys.path.append("..")
from model.Trabajador import Trabajador
from tkinter import *
from controllers.producto_controller import get_productos,set_productos,total_productos

    
class VentanaProducto:
    def __init__(self,root) -> None:
        self.root =  root
        self.root.title('Ventana Producto')
        self.set_window()

    #Funciones
    def save_new_client(self,nombre,email,edad,telefono,direccion):
        total= total_productos()
        trabajador = Trabajador(total+1,nombre,email,edad,telefono,direccion)
        set_productos(trabajador)
        self.display_products()

    def display_products(self,):
        trabajadores = get_productos()
        listbox = Listbox(self.frame,width=100,height=5)
        listbox.grid(row=10,columnspan=4,sticky=W+E)

        for trabajador in trabajadores:
            print(trabajador)
            listbox.insert(END,trabajador)

    def set_window(self):
        #Canvas
        canvas = Canvas(self.root,height=900,width=900)
        canvas.pack()


        self.frame = Frame()
        self.frame.place(relx=0.1,rely=0.1,relwidth=0.9,relheight=0.8,width=500)

        label_name = Label(self.frame,text='Agregar Nuevo Cliente')
        label_name.grid(row=0,column=1)

        ## Input Nombre
        label_name = Label(self.frame,text='Nombre')
        label_name.grid(row=1,column=0)
        entry_name = Entry(self.frame)
        entry_name.grid(row=1,column=1)

        ##Input Email
        label_precio = Label(self.frame,text='Precio')
        label_precio.grid(row=2,column=0)
        entry_precio = Entry(self.frame)
        entry_precio.grid(row=2,column=1)

        button = Button(self.frame,text='Agregar',command=lambda: self.save_new_client(
            entry_name.get(),
            entry_precio.get(),

        ))
        button.grid(row=6,column=1,sticky=W+E)


        self.display_products()

        