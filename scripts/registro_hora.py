
import os
from datetime import datetime
import pytz

# Nombre del archivo donde se guardarán los registros
filename = "../registros.txt"

# Función para leer los registros actuales desde el archivo
def leer_registros(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            registros = file.readlines()
        return [registro.strip() for registro in registros]
    return []

# Función para escribir los registros en el archivo
def escribir_registros(filename, registros):
    with open(filename, "w") as file:
        for registro in registros:
            file.write(registro + "\n")

# Obtener la hora actual en la zona horaria de América/Santiago
timezone = pytz.timezone("America/Santiago")
hora_actual = datetime.now(timezone).strftime("%d/%m/%Y %H:%M")

# Leer los registros actuales
registros = leer_registros(filename)

# Agregar la hora actual a los registros
registros.append(hora_actual)

# Mantener solo los últimos 4 registros
if len(registros) > 4:
    registros = registros[-4:]

# Escribir los registros actualizados en el archivo
escribir_registros(filename, registros)

print("Registro actualizado con éxito.")