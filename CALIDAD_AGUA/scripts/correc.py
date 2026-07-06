# IMPORTAR LIBRERIAS
import pandas as pd
import numpy as np

# DEFINE LA RUTA
carpeta = "C:\\Users\\brv_1\\Documents\\Programacion\\PORTAFOLIOS\\DASHBOARDS2\\CALIDAD_AGUA\\database"
archivo = "\\Base_Calidad_Agua_Profesional.xlsx"
ruta = carpeta + archivo

# LEER EL ARCHIVO
df = pd.read_excel(ruta, sheet_name = "Monitoreo")
# ELIMINAR DUPLICADOS
df = df.drop_duplicates()
# CONVIERTE FECHA
df['Fecha'] = pd.to_datetime(df['Fecha'])
# ELIMINA VACIOS
df.fillna(df.mean(numeric_only=True), inplace=True)

# GUARDA EL ARCHVO CORREGIDO EN LA MISMA RUTA
carpeta_clean = "C:\\Users\\brv_1\\Documents\\Programacion\\PORTAFOLIOS\\DASHBOARDS2\\CALIDAD_AGUA\\database\\clean"
nuevo_nombre = "\\Base_Calidad_Agua_Profesional_clean.xlsx"
ruta_guardar = carpeta_clean + nuevo_nombre
df.to_excel(ruta_guardar, index=False)

