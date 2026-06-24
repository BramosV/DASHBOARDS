# IMPORTAR LIBRERIAS
import pandas as pd

# DEFINE LA RUTA
ruta = r"C:\Users\brv_1\Documents\Programacion\PORTAFOLIOS\DASHBOARDS\CALIDAD_AGUA\database\Base_Calidad_Agua_5000_Registros_PRB.csv"

# LEER EL ARCHIVO
df = pd.read_csv(ruta)
# ELIMINAR DUPLICADOS
df = df.drop_duplicates()
# CONVIERTE FECHA
df['Fecha'] = pd.to_datetime(df['Fecha'])
# ELIMINA VACIOS
df.fillna(df.mean(numeric_only=True), inplace=True)
# GUARDA EL ARCHVO CORREGIDO EN LA MISMA RUTA
df.to_csv(r'C:\Users\brv_1\Documents\Programacion\PORTAFOLIOS\DASHBOARDS\CALIDAD_AGUA\database\clean\Clean_data.csv', index=False)