import sys
sys.path.append("..")
from model.Trabajador import Trabajador
from tkinter import *
from controllers.producto_controller import get_productos

root =  Tk()
root.title('Ventana Cliente')

#Funciones
def save_new_client(nombre,email,edad,telefono,direccion):
    total= total_trabajadores()
    trabajador = Trabajador(total+1,nombre,email,edad,telefono,direccion)
    set_trabajadores(trabajador)
    display_clients()

def display_clients():
    trabajadores = get_trabajadores()
    listbox = Listbox(frame,width=100,height=5)
    listbox.grid(row=10,columnspan=4,sticky=W+E)

    for trabajador in trabajadores:
        print(trabajador)
        listbox.insert(END,trabajador)


#Canvas
canvas = Canvas(root,height=900,width=900)
canvas.pack()


frame = Frame()
frame.place(relx=0.1,rely=0.1,relwidth=0.9,relheight=0.8,width=500)

label_name = Label(frame,text='Agregar Nuevo Cliente')
label_name.grid(row=0,column=1)

## Input Nombre
label_name = Label(frame,text='Nombre')
label_name.grid(row=1,column=0)
entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

##Input Email
label_precio = Label(frame,text='Precio')
label_precio.grid(row=2,column=0)
entry_precio = Entry(frame)
entry_precio.grid(row=2,column=1)

button = Button(frame,text='Agregar',command=lambda: save_new_client(
    entry_name.get(),
    entry_precio.get(),

))
button.grid(row=6,column=1,sticky=W+E)


display_clients()

root.mainloop()