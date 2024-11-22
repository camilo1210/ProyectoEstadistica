import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos ficticios para referencia
data_barras = {
    "Referencia": ["Ref1", "Ref2", "Ref3", "Ref4", "Ref5"],
    "Total Producción": [1000, 800, 950, 1100, 900],
    "Total pérdida": [50, 60, 40, 70, 80]
}

# Crear DataFrame
df_barras = pd.DataFrame(data_barras)

# Configurar posiciones para las barras
x = np.arange(len(df_barras["Referencia"]))  # Rango de posiciones
ancho = 0.4  # Ancho de las barras

# Crear gráfica de barras
plt.figure(figsize=(10, 6))
plt.bar(x - ancho / 2, df_barras["Total Producción"], width=ancho, color='blue', label="Producción Total")
plt.bar(x + ancho / 2, df_barras["Total pérdida"], width=ancho, color='red', label="Pérdida Total")

# Añadir etiquetas de porcentaje de pérdida encima de las barras
for i in range(len(df_barras)):
    perdida_pct = (df_barras["Total pérdida"][i] / df_barras["Total Producción"][i]) * 100
    plt.text(x[i] + ancho / 2, df_barras["Total pérdida"][i] + 5, f"{perdida_pct:.1f}%", 
             ha='center', fontsize=9, color='red')

# Configurar etiquetas y título
plt.xlabel("Referencia")
plt.ylabel("Unidades")
plt.title("Producción Total vs. Pérdida Total por Referencia")
plt.xticks(x, df_barras["Referencia"])  # Etiquetas en el eje X
plt.legend()

# Ajustar diseño y mostrar gráfica
plt.tight_layout()
plt.show()
