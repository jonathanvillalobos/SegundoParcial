import tkinter as tk 

#creamos la ventgana principal
def saludo():
    label_resultado.config(text="Hola alumnos de python")
    
ventana= tk.Tk()
#le damoss un titulo a la ventana
ventana.title("Mi primera aplicacion")
#Le damos un tamano a la ventana 
ventana.geometry("480x300")
#creamos el boton
boton=tk.Button(ventana,text="saludar",command=saludo)
boton.pack(pady=20)
#mostramos la etiqueta en la ventana 
label_resultado = tk.Label(ventana, text= "Hola mundo", font=("Arial", 16,"bold"))
label_resultado.pack(pady=20)

#Iniciamos la etiqueta ventana 
ventana.mainloop()
