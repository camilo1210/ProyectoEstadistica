import pandas as pd

# Datos obtenidos de la imagen proporcionada
data = {
    "Referencia": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12", "P13", "P14", "Total"],
    "Total Producción": [1440, 1440, 240, 3360, 720, 720, 2400, 2400, 450, 2400, 720, 720, 1800, 720, 19530],
    "Devoluciones": [20, 12, 15, 60, 30, 25, 40, 45, 20, 50, 15, 20, 55, 36, 443],
    "Desechos": [35, 40, 25, 100, 50, 40, 60, 70, 22, 110, 18, 35, 60, 44, 709],
    "Total pérdida": [55, 52, 40, 160, 80, 65, 100, 115, 42, 160, 33, 55, 115, 80, 1152],
    "% pérdida": [4, 4, 17, 5, 11, 9, 4, 5, 9, 7, 5, 8, 6, 11, 6]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Guardar el DataFrame como archivo CSV
csv_path = "/mnt/data/analisis_produccion.csv"
df.to_csv(csv_path, index=False)

# Ahora realizamos un análisis básico de las pérdidas y porcentajes
analisis = {
    "Producción Total": df["Total Producción"].sum(),
    "Devoluciones Totales": df["Devoluciones"].sum(),
    "Desechos Totales": df["Desechos"].sum(),
    "Pérdida Total": df["Total pérdida"].sum(),
    "Porcentaje Medio de Pérdida": df.loc[df["Referencia"] != "Total", "% pérdida"].mean()
}

# Mostrar el análisis
analisis, csv_path
