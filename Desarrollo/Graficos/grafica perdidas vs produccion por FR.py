import matplotlib.pyplot as plt

# Configurar los datos para la gráfica
referencias = df["Referencia"][:-1]  # Excluir la fila "Total"
produccion_total = df["Total Producción"][:-1]
perdida_total = df["Total pérdida"][:-1]

# Crear la gráfica de barras para producción y pérdida total
plt.figure(figsize=(10, 6))
plt.bar(referencias, produccion_total, color='blue', label="Producción Total")
plt.bar(referencias, perdida_total, color='red', label="Pérdida Total")

# Añadir etiquetas y título
plt.xlabel("Referencia")
plt.ylabel("Unidades")
plt.title("Producción Total vs Pérdida Total por Referencia")
plt.legend()

# Mostrar la gráfica
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
