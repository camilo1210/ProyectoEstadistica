import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel
excel_path = "Desarrollo/devoluciones_pan.xlsx"

# Cargar los datos desde el archivo Excel
df = pd.read_excel(excel_path)

# Verificar las columnas cargadas
print("Columnas cargadas:", df.columns)

# Verificar las primeras filas de los datos cargados
print(df.head())

# Crear la gráfica de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(df["%"], df["Cantidad"], color='blue')

# Añadir etiquetas y título
plt.title('Dispersión de Causas de Devolución de Pan')
plt.xlabel('Porcentaje (%)')
plt.ylabel('Cantidad')
plt.grid(True)

# Etiquetas para los puntos en la gráfica
for i in range(len(df)):
    # Usamos el nombre correcto de la columna
    plt.text(df["%"][i], df["Cantidad"][i], df["Causas de devolucion"][i], fontsize=9)

# Mostrar la gráfica
plt.show()

# Datos ficticios para las causas de devolución (para el archivo CSV)
data = {
    "Causas de devolución": [
        " Pan duro ", " Mala Presentación ", " Pan dañado o aplastado ", " Pan con mal olor ",
        " Pan baboso ", " Pan con moho ", " Pan sin relleno ", " Pan con mala textura ",
        " Pan crudo ", " Pan quemado ", " Pan con malsabor ", " No venta ", " Otros " 
    ],
    "%": [24, 3, 10, 5, 2, 21, 2, 5, 2, 10, 1, 13, 2],
    "Cantidad": [278, 10, 120, 61, 27, 237, 20, 54, 20, 118, 37, 150, 20]
}

# Crear el DataFrame
df_devoluciones = pd.DataFrame(data)

# Guardar los datos en un archivo CSV
csv_path = "causas_devoluciones.csv"
df_devoluciones.to_csv(csv_path, index=False)

print(f"Datos guardados en {csv_path}")
