import tkinter as tk 

#creamos la ventgana principal
ventana= tk.Tk()
#le damoss un titulo a la ventana
ventana.title("Mi primera aplicacion")
#Le damos un tamano a la ventana 
ventana.geometry("480x300")

#mostramos la etiqueta en la ventana 
etiqueta = tk.Label(ventana, text= "Hola mundo", font=("Arial", 16,"bold"))
etiqueta.pack(pady=20)

#Iniciamos la etiqueta ventana 
ventana.mainloop()
