import matplotlib.pyplot as plt

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
    plt.text(df["%"][i], df["Cantidad"][i], df["Causas de devolución"][i], fontsize=9)

# Mostrar la gráfica
plt.show()
