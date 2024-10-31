import pandas as pd

# Crear un DataFrame con los datos proporcionados
data = {
    "Causas de devolución": [
        "Pan duro", "Mala Presentación", "Pan dañado o aplastado", "Pan con mal olor",
        "Pan baboso", "Pan con moho", "Pan sin relleno", "Pan con mala textura",
        "Pan crudo", "Pan quemado", "Pan con malsabor", "No venta", "Otros"
    ],
    "%": [24, 3, 10, 5, 2, 21, 2, 5, 2, 10, 1, 13, 2],
    "Cantidad": [278, 10, 120, 61, 27, 237, 20, 54, 20, 118, 37, 150, 20]
}

df = pd.DataFrame(data)

# Guardar los datos en un archivo CSV
file_path = '/mnt/data/devoluciones_pan.csv'
df.to_csv(file_path, index=False)

df.head(), file_path
