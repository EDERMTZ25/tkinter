from tkinter import TK, Button, Frame

#1
ventana=TK()
ventana.title= ("EJEMPLO DE 3 FRAMES")
ventana.geometry("600x400")


#2
seccion1=Frame(ventana,bg="red")
seccion1.pack(expand=True, fill='both')

seccion2=Frame(ventana,bg="green")
seccion2.pack(expand=True, fill='both')
seccion3=Frame(ventana,bg="yellow")
seccion3.pack(expand=True, fill='both')

#3 Botones
botonAzul=Button(seccion1, text="Boton Azul", fg="blue")
botonAzul.place(x="60", y="60")

botonnNegro=Button(seccion2, text="Boton Negro", fg="white")
botonnNegro.grid(row=0, column=0)

botonVerde=Button(seccion1, text="BotonAzul", fg="blue")
botonVerde.place(x="60", y="60")





#4
ventana.mainloop()
