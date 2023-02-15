import pymysql

# Abrir la conexión a la base de datos
db = pymysql.connect(host="localhost", user="root", password="Fhanser1989", db="padron2023")
cursor = db.cursor()

# Leer el archivo y procesar cada línea
with open('usuarios.txt', 'r') as file:
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
