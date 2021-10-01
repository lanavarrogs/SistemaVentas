import sys
sys.path.append("..")
from tkinter import *

root =  Tk()
root.title('Ventana Cliente')

def set_visible():
    root.withdraw()


canvas = Canvas(root,height=900,width=900)
canvas.pack()


frame = Frame()
frame.place(relx=0.1,rely=0.1,relwidth=0.9,relheight=0.8,width=500)


button = Button(frame,text='Agregar',command=lambda: set_visible())
button.grid(row=6,column=1,sticky=W+E)




root.mainloop()