# -*- coding: utf-8 -*-
"""
Created on Feb 2023

@author: Fernand J.Hanser
"""

import tkinter as tk
from tkinter import messagebox
from faker import Faker
import random


root = tk.Tk()
# Establecer la posición de la ventana
root.title("Generador de usuarios masivos 1.0")
root.geometry("400x200")

def generar_usuarios():
    num_registros = int(entry.get())
    fake = Faker()
    with open("usuariosFake.txt", "w") as f: #Nombre del archivo
        for i in range(num_registros):
            cui = str(random.randint(1000000000000, 9999999999999))
            nombre_completo = fake.name().replace(',', '')
            fecha_de_nacimiento = fake.date().replace(',', '')
            centro_de_votacion = fake.address().replace(',', '').replace('\n', '')
            departamento = fake.city().replace(',', '')
            municipio = fake.state().replace(',', '')
            f.write("{},{},{},{},{},{}\n".format(cui, nombre_completo,fecha_de_nacimiento, centro_de_votacion, departamento, municipio))
    messagebox.showinfo("Usuarios Generados", f"{num_registros} usuarios generados con éxito")
    root.destroy()

# Crear el widget Label para mostrar la instrucción
label = tk.Label(root, text="Ingrese la cantidad de usuarios:")
label.pack(pady=25)

entry = tk.Entry(root, width=10)
entry.pack()

# Crear el widget Button para generar los usuarios
button = tk.Button(root, text="Generar", command=generar_usuarios)
button.pack(pady=25)


root.update_idletasks()
# Obtener el ancho y la altura de la pantalla
w = root.winfo_width()
h = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (w // 2)
y = (root.winfo_screenheight() // 2) - (h // 2)
root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

# Mostrar la ventana principal
root.mainloop()



