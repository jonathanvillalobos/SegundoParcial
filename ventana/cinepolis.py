import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def procesar():
    nombre = entry_nombre.get()
    personas = int(entry_personas.get())
    boletos = int(entry_boletos.get())
    tarjeta = tarjeta_var.get()

    precio_boleto = 12
    max_boletos = personas * 7

    if boletos > max_boletos:
        messagebox.showerror("Error", f"Máximo {max_boletos} boletos para {personas} personas")
        return

    total = boletos * precio_boleto

    # Descuento por cantidad
    if boletos > 5:
        total *= 0.85
    elif boletos >= 4:
        total *= 0.90

    # Descuento por tarjeta
    if tarjeta == "Si":
        total *= 0.90

    salida_valor.config(text=f"${total:.2f}")
    


# Ventana
ventana = tk.Tk()
ventana.title("Cinépolis")
ventana.geometry("450x300")

# cargar imagen
imagen = Image.open("cineploisimagen.png")
imagen = imagen.resize((450,300))  # mismo tamaño que la ventana
fondo = ImageTk.PhotoImage(imagen) 
label_fondo = tk.Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Entradas
tk.Label(ventana, text="Nombre").grid(row=4, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=4, column=1)

tk.Label(ventana, text="Cantidad de Personas").grid(row=5, column=0)
entry_personas = tk.Entry(ventana)
entry_personas.grid(row=5, column=1)

tk.Label(ventana, text="Cantidad de Boletos").grid(row=6, column=0)
entry_boletos = tk.Entry(ventana)
entry_boletos.grid(row=6, column=1)

# Tarjeta
tarjeta_var = tk.StringVar(value="No")

tk.Label(ventana, text="Tarjeta CINECO").grid(row=7, column=0)
tk.Radiobutton(ventana, text="Si", variable=tarjeta_var, value="Si").grid(row=7, column=1)
tk.Radiobutton(ventana, text="No", variable=tarjeta_var, value="No").grid(row=7, column=2)

# Salida
tk.Label(ventana, text="Valor a pagar").grid(row=8, column=0)
salida_valor = tk.Label(ventana, text="$0")
salida_valor.grid(row=8, column=1)

# Botones
tk.Button(ventana, text="Procesar", command=procesar).grid(row=9, column=0)
tk.Button(ventana, text="Salir", command=ventana.quit).grid(row=9, column=1)

ventana.mainloop()