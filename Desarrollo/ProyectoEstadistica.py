import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#==================================================================================================
# Cargar el archivo de Excel
file_path_Ventas = '/home/camilo/UNIVALLE/SEMESTRE 4/ESTADISTICA/proyecto estadistica/ProyectoEstadistica/Desarrollo/datos Informe de ventas Pan & Arte Yumbo.xlsx'
ventas_df = pd.read_excel(file_path_Ventas, sheet_name='Datos de ventas', skiprows=1)

file_path_Desperdicios ='/home/camilo/UNIVALLE/SEMESTRE 4/ESTADISTICA/proyecto estadistica/ProyectoEstadistica/Desarrollo/devoluciones_pan.xlsx'
desperdicio_df = pd.read_excel(file_path_Desperdicios, sheet_name='Datos de desperdicio', skiprows=0)
#==================================================================================================


#==================================================================================================
# Extraer datos para cálculos de desperdicio y ventas
ventas = ventas_df['Total']
desperdicio = desperdicio_df['Cantidad']



#mirar Columnas vacias
ventas_df.dropna(subset=['Total'], inplace=True)
desperdicio_df.dropna(subset=['Causas de devolucion'], inplace=True)


# Renombrar columnas para simplificar (ajusta según el formato de las hojas)
ventas_df.columns = ['Index', 'Producto', 'Cliente', '1er_trim', '2do_trim', '3er_trim', '4to_trim', 'Total', 'Extra']
desperdicio_df.columns = ['Causas de devolucion', '%', 'Cantidad']

# Eliminar columnas innecesarias
ventas_df = ventas_df.drop(columns=['Index', 'Extra'])

# Convertir columnas a numérico
ventas_df[['1er_trim', '2do_trim', '3er_trim', '4to_trim', 'Total']] = ventas_df[
    ['1er_trim', '2do_trim', '3er_trim', '4to_trim', 'Total']].apply(pd.to_numeric, errors='coerce')

# Filtrar filas con Total > 0 para evitar divisiones por cero
ventas_df = ventas_df[ventas_df['Total'] > 0]
#==================================================================================================

#==================================================================================================
# Cálculo de métricas para ventas por trimestre y total
promedios = ventas_df[['1er_trim', '2do_trim', '3er_trim', '4to_trim', 'Total']].mean()
desviaciones = ventas_df[['1er_trim', '2do_trim', '3er_trim', '4to_trim', 'Total']].std()

# Calcular el porcentaje de ventas de cada trimestre respecto al total
porcentajes = ventas_df[['1er_trim', '2do_trim', '3er_trim', '4to_trim']].div(ventas_df['Total'], axis=0) * 100
porcentajes_medios = porcentajes.mean()

# Calcular estadísticas para ventas
ventas_promedio = ventas.mean()
ventas_mediana = ventas.median()
ventas_desviacion_std = ventas.std()
ventas_rango = ventas.max() - ventas.min()

# Calcular estadísticas para desperdicio
desperdicio_promedio = desperdicio.mean()
desperdicio_mediana = desperdicio.median()
desperdicio_desviacion_std = desperdicio.std()
desperdicio_rango = desperdicio.max() - desperdicio.min()

# Calcular el porcentaje de desperdicio en relación con las ventas
porcentaje_desperdicio = (desperdicio / ventas) * 100
porcentaje_desperdicio_promedio = porcentaje_desperdicio.mean()
#==================================================================================================

#==================================================================================================
# Mostrar resultados
print("Promedio de Ventas por Trimestre y Total:")
print(promedios)

print("\nDesviación Estándar de Ventas por Trimestre y Total:")
print(desviaciones)

print("\nPorcentaje Promedio de Ventas de cada Trimestre respecto al Total:")
print(porcentajes_medios)

print("\nEstadísticas de Ventas:")
print(f"Promedio: {ventas_promedio}")
print(f"Mediana: {ventas_mediana}")
print(f"Desviación Estándar: {ventas_desviacion_std}")
print(f"Rango: {ventas_rango}")

print("\nEstadísticas de Desperdicio:")
print(f"Promedio: {desperdicio_promedio}")
print(f"Mediana: {desperdicio_mediana}")
print(f"Desviación Estándar: {desperdicio_desviacion_std}")
print(f"Rango: {desperdicio_rango}")
print(f"Promedio del Porcentaje de Desperdicio: {porcentaje_desperdicio_promedio}%")

# Visualización de la distribución del porcentaje de desperdicio
plt.figure(figsize=(10, 5))
sns.histplot(porcentaje_desperdicio, kde=True, color='purple')
plt.title("Distribución del Porcentaje de Desperdicio")
plt.xlabel("Porcentaje de Desperdicio")
plt.ylabel("Frecuencia")
plt.show()

