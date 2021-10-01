import sys
sys.path.append("..")
from model.Cliente import Cliente
from tkinter import *
from controllers.cliente_controller import get_clientes,set_clientes,total_clients

root =  Tk()
root.title('Ventana Cliente')
clients = []

#Funciones
def save_new_client(nombre,email,edad,telefono,direccion):
    total= total_clients()
    cliente = Cliente(total+1,nombre,email,edad,telefono,direccion)
    set_clientes(cliente)
    display_clients()

def display_clients():
    clients = get_clientes()
    listbox = Listbox(frame,width=100,height=5)
    listbox.grid(row=10,columnspan=4,sticky=W+E)

    for client in clients:
        print(client)
        listbox.insert(END,client)


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
label_email = Label(frame,text='Email')
label_email.grid(row=2,column=0)
entry_email = Entry(frame)
entry_email.grid(row=2,column=1)

##Input edad
label_edad = Label(frame,text='Edad')
label_edad.grid(row=3,column=0)
entry_edad = Entry(frame)
entry_edad.grid(row=3,column=1)

##Input telefono
label_telefono = Label(frame,text='Telefono')
label_telefono.grid(row=4,column=0)
entry_telefono = Entry(frame)
entry_telefono.grid(row=4,column=1)

##Input direccion
label_direccion = Label(frame,text='Direccion')
label_direccion.grid(row=5,column=0)
entry_direccion = Entry(frame)
entry_direccion.grid(row=5,column=1)

button = Button(frame,text='Agregar',command=lambda: save_new_client(
    entry_name.get(),
    entry_email.get(),
    entry_edad.get(),
    entry_telefono.get(),
    entry_direccion.get()
))
button.grid(row=6,column=1,sticky=W+E)


display_clients()

root.mainloop()