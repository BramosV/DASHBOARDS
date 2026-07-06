import pandas as pd
import numpy as np

# DEFINE LA RUTA, SE USARÁ ARCHIVO CORREGIDO Y LIMPIO
carpeta = "C:\\Users\\brv_1\\Documents\\Programacion\\PORTAFOLIOS\\DASHBOARDS2\\CALIDAD_AGUA\\database\\clean"
archivo = "\\Base_Calidad_Agua_Profesional_clean.xlsx"
ruta = carpeta + archivo

# Leer archivo
df = pd.read_excel(ruta)

# Cumplimiento pH
# Crea la columna
df['Cumpl_pH'] = np.nan
# Aplica la condicion
df['Cumpl_pH'] = np.where(
    (df['pH'] > 6.5) & (df['pH'] < 8.5),
    0,
    1
)
#df['Cumpl_pH'] = df['pH'].between(6.5, 8.5).astype(int)
# Cumplimiento de OD
df['Cumpl_OD'] = np.nan
df['Cumpl_OD'] = np.where(df['OD'] > 4, 0, 1)
# Cumplimiento Conductividad
df['Cumpl_CE'] = np.nan
df['Cumpl_CE'] = np.where(df['Conductividad'] < 1000, 0, 1)
# Cumplimiento Nitratos
df['Cumpl_NO3'] = np.nan
df['Cumpl_NO3'] = np.where(df['Nitratos'] < 100, 0, 1)
# Cumplimiento Fosfatos
df['Cumpl_PO4'] = np.nan
df['Cumpl_PO4'] = np.where(df['Fosfatos'] < 5, 0, 1)
# Cumplimiento Arsénico
df['Cumpl_As'] = np.nan
df['Cumpl_As'] = np.where(df['Arsenico'] < 0.1, 0, 1)

# GUARDA EL ARCHVO CORREGIDO EN LA MISMA RUTA
carpeta_final = "C:\\Users\\brv_1\\Documents\\Programacion\\PORTAFOLIOS\\DASHBOARDS2\\CALIDAD_AGUA\\database\\final"
nuevo_nombre = "\\Base_Calidad_Agua_Profesional_final.xlsx"
ruta_guardar = carpeta_final + nuevo_nombre
df.to_excel(ruta_guardar, index=False)