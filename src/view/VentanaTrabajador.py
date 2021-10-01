import sys
sys.path.append("..")
from model.Trabajador import Trabajador
from tkinter import *
from controllers.trabajador_controller import get_trabajadores,set_trabajadores,total_trabajadores

class VentanaTrabajador:

    def __init__(self,root) -> None:
        self.root =  root
        self.root.title('Ventana Cliente')
        self.set_window()

    #Funciones
    def save_new_client(self,nombre,email,edad,telefono,direccion):
        total= total_trabajadores()
        trabajador = Trabajador(total+1,nombre,email,edad,telefono,direccion)
        set_trabajadores(trabajador)
        self.display_workers()

    def display_workers(self):
        trabajadores = get_trabajadores()
        listbox = Listbox(self.frame,width=100,height=5)
        listbox.grid(row=10,columnspan=4,sticky=W+E)

        for trabajador in trabajadores:
            print(trabajador)
            listbox.insert(END,trabajador)

    def set_window(self):
        #Canvas
        self.canvas = Canvas(self.root,height=900,width=900)
        self.canvas.pack()


        self.frame = Frame()
        self.frame.place(relx=0.1,rely=0.1,relwidth=0.9,relheight=0.8,width=500)

        label_name = Label(self.frame,text='Agregar Nuevo Trabajador')
        label_name.grid(row=0,column=1)

        ## Input Nombre
        label_name = Label(self.frame,text='Nombre')
        label_name.grid(row=1,column=0)
        entry_name = Entry(self.frame)
        entry_name.grid(row=1,column=1)

        ##Input Email
        label_email = Label(self.frame,text='Email')
        label_email.grid(row=2,column=0)
        entry_email = Entry(self.frame)
        entry_email.grid(row=2,column=1)

        ##Input edad
        label_edad = Label(self.frame,text='Edad')
        label_edad.grid(row=3,column=0)
        entry_edad = Entry(self.frame)
        entry_edad.grid(row=3,column=1)

        ##Input telefono
        label_telefono = Label(self.frame,text='Telefono')
        label_telefono.grid(row=4,column=0)
        entry_telefono = Entry(self.frame)
        entry_telefono.grid(row=4,column=1)

        ##Input direccion
        label_direccion = Label(self.frame,text='Direccion')
        label_direccion.grid(row=5,column=0)
        entry_direccion = Entry(self.frame)
        entry_direccion.grid(row=5,column=1)

        button = Button(self.frame,text='Agregar',command=lambda: self.save_new_client(
            entry_name.get(),
            entry_email.get(),
            entry_edad.get(),
            entry_telefono.get(),
            entry_direccion.get()
        ))
        button.grid(row=6,column=1,sticky=W+E)


        self.display_workers()