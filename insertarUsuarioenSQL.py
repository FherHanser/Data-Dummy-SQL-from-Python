import tkinter as tk
from tkinter import filedialog
import pymysql

def probar_conexion():
    # Recuperar los valores de los cuadros de entrada
    host = host_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    db_name = db_entry.get()

    try:
        # Intentar conectarse a la base de datos con los valores proporcionados
        db = pymysql.connect(host=host, user=user, password=password, db=db_name)
        db.close()

        # Mostrar un mensaje de éxito
        exito_label.config(text="La conexión es válida")
        
        # Enable the "Procesar" button and set a flag to indicate a successful connection
        procesar_button.config(state=tk.NORMAL)
        global conexion_valida
        conexion_valida = True
    except Exception as e:
        # Mostrar un mensaje de error
        exito_label.config(text=f"Error de conexión: {str(e)}")


def procesar_archivo():
    # Abrir el diálogo de selección de archivo
    archivo = filedialog.askopenfilename()

    if archivo:
        # Recuperar los valores de los cuadros de entrada
        host = host_entry.get()
        user = user_entry.get()
        password = password_entry.get()
        db_name = db_entry.get()

        try:
            # Intentar conectarse a la base de datos con los valores proporcionados
            db = pymysql.connect(host=host, user=user, password=password, db=db_name)
            cursor = db.cursor()

            # Leer el archivo y procesar cada línea
            with open(archivo, 'r') as file:
                for line in file:
                    fields = line.strip().split(',') # Separar los campos de la línea

                    # Verificar si la lista fields tiene suficientes elementos
                    if len(fields) < 5:
                        print(f"La línea '{line}' no tiene suficientes elementos para ser procesada")
                        continue

                    cui = fields[0]
                    nombre_completo = fields[1]
                    centro_votacion = fields[2]
                    departamento = fields[3]
                    municipio = fields[4]

                    # Insertar los datos en la tabla "usuarios"
                    query = f"INSERT INTO ciudadanos (cui, nombre_completo, centro_de_votacion, departamento, municipio) VALUES ('{cui}', '{nombre_completo}', '{centro_votacion}', '{departamento}', '{municipio}')"
                    cursor.execute(query)

            # Cerrar la conexión a la base de datos
            db.commit()
            db.close()

            # Mostrar un mensaje de éxito
            exito_label.config(text=f"{len(fields)} usuarios generados con éxito")
        except Exception as e:
            # Mostrar un mensaje de error
            exito_label.config(text=f"Error: {str(e)}")

# Crear la ventana principal
root = tk.Tk()
root.title("Establecer conexion a la Base de Datos")

# Establecer tamaño y centrar ventana
window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.update_idletasks()
root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())


# Crear los cuadros de entrada para los valores de conexión
host_label = tk.Label(root, text="Host:")
host_label.pack()
host_entry = tk.Entry(root)
host_entry.pack()

user_label = tk.Label(root, text="Usuario:")
user_label.pack()
user_entry = tk.Entry(root)
user_entry.pack()

password_label = tk.Label(root, text="Contraseña:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

db_label = tk.Label(root, text="Base de datos:")
db_label.pack()
db_entry = tk.Entry(root)
db_entry.pack()

# Crear un botón para conectarse
conectar_button = tk.Button(root, text="Probar conexión", command=probar_conexion)
conectar_button.pack()

# Crear un botón para procesar el archivo (inicialmente deshabilitado)
procesar_button = tk.Button(root, text="Procesar archivo", command=procesar_archivo, state=tk.DISABLED)
procesar_button.pack()


# Crear una etiqueta para mostrar el resultado
exito_label = tk.Label(root, text="")
exito_label.pack()

root.mainloop()
