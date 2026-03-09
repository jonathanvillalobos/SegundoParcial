import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")

opciones = ("Mexico", "Colombia", "Peru", "Chile")

combo = ttk.Combobox(root, values=opciones)
combo.pack (pady=20)

def obtener():
    Label_resultado.config(text=combo.get())
    print(combo.get())
    
btn= tk.Button(root, text="Obtener", command= obtener)
btn.pack()

Label_resultado = tk.Label(root, text="", font= ("Arial", 16, "bold"))
Label_resultado.pack(pady=20)
    

root.mainloop()
