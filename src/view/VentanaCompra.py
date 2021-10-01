import sys
sys.path.append("..")
from tkinter import *
from model.Venta import Venta
from controllers.venta_controller import get_ventas,total_ventas,set_ventas,get_precio_producto


class VentanaCompra:

    def __init__(self,root) -> None:
        self.root = root
        self.set_window()


    def set_venta(self,trabajador,producto,estaus,sucursal,cliente,total_precio):
        total= total_ventas()
        trabajador = Venta(total+1,estaus,total_precio,sucursal,cliente,trabajador,producto)
        set_ventas(trabajador)
        self.display_ventas()

        
    #Funciones
    def display_ventas(self):
        trabajadores = get_ventas()
        listbox = Listbox(self.frame,width=100,height=5)
        listbox.grid(row=10,columnspan=4,sticky=W+E)

        for trabajador in trabajadores:
            print(trabajador)
            listbox.insert(END,trabajador)

    def set_window(self):
        canvas = Canvas(self.root,height=900,width=900)
        canvas.pack()


        self.frame = Frame()
        self.frame.place(relx=0.1,rely=0.1,relwidth=0.9,relheight=0.8,width=500)

        label_vendedor = Label(self.frame,text='Agregar Vendedor')
        label_vendedor.grid(row=2,column=0)
        entry_vendedor = Entry(self.frame)
        entry_vendedor.grid(row=2,column=1)

        label_cliente = Label(self.frame,text='Agregar Cliente')
        label_cliente.grid(row=3,column=0)
        entry_cliente = Entry(self.frame)
        entry_cliente.grid(row=3,column=1)

        label_producto = Label(self.frame,text='Agregar Producto')
        label_producto.grid(row=4,column=0)
        entry_producto = Entry(self.frame)
        entry_producto.grid(row=4,column=1)

        label_status = Label(self.frame,text='Agregar Status de compra')
        label_status.grid(row=5,column=0)
        entry_status = Entry(self.frame)
        entry_status.grid(row=5,column=1)

        label_sucursal = Label(self.frame,text='Agregar Sucursal')
        label_sucursal.grid(row=6,column=0)
        entry_sucursal = Entry(self.frame)
        entry_sucursal.grid(row=6,column=1)

        label_total = Label(self.frame,text='Agregar Total')
        label_total.grid(row=7,column=0)
        entry_total = Entry(self.frame)
        entry_total.grid(row=7,column=1)

        button = Button(self.frame,text='comprar',command=lambda: self.set_venta(
            entry_vendedor.get(),
            entry_producto.get(),
            entry_status.get(),
            entry_sucursal.get(),
            entry_cliente.get(),
            entry_total.get()
        ))
        button.grid(row=8,column=1,sticky=W+E)

        self.display_ventas()
