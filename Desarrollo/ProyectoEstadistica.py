import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ==============================
# Función para cargar datos
# ==============================
def cargar_datos():
    try:
        # Cargar ventas
        file_path_ventas = 'Desarrollo/datos Informe de ventas Pan & Arte Yumbo.xlsx'
        ventas_df = pd.read_excel(file_path_ventas, sheet_name='Datos de ventas', skiprows=1)

        # Cargar desperdicios
        file_path_desperdicios = 'Desarrollo/devoluciones_pan.xlsx'
        desperdicio_df = pd.read_excel(file_path_desperdicios, sheet_name='Datos de desperdicio', skiprows=0)

        # Procesar datos
        ventas_df.dropna(subset=['Total'], inplace=True)
        desperdicio_df.dropna(subset=['Causas de devolucion'], inplace=True)
        ventas_df.columns = ['Index', 'Producto', 'Cliente', '1er_trim', '2do_trim', '3er_trim', '4to_trim', 'Total', 'Extra']
        desperdicio_df.columns = ['Causas de devolucion', '%', 'Cantidad']
        ventas_df = ventas_df.drop(columns=['Index', 'Extra'])
        ventas_df[['1er_trim', '2do_trim', '3er_trim', '4to_trim', 'Total']] = ventas_df[
            ['1er_trim', '2do_trim', '3er_trim', '4to_trim', 'Total']].apply(pd.to_numeric, errors='coerce')
        ventas_df = ventas_df[ventas_df['Total'] > 0]

        return ventas_df, desperdicio_df
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar los datos: {e}")
        return None, None


# ==============================
# Función para calcular métricas
# ==============================
def calcular_metricas(ventas_df, desperdicio_df):
    ventas = ventas_df['Total']
    desperdicio = desperdicio_df['Cantidad']

    # Calcular estadísticas
    promedios = ventas_df[['1er_trim', '2do_trim', '3er_trim', '4to_trim', 'Total']].mean()
    desviaciones = ventas_df[['1er_trim', '2do_trim', '3er_trim', '4to_trim', 'Total']].std()
    porcentajes = ventas_df[['1er_trim', '2do_trim', '3er_trim', '4to_trim']].div(ventas_df['Total'], axis=0) * 100
    porcentajes_medios = porcentajes.mean()
    porcentaje_desperdicio = (desperdicio / ventas) * 100

    return {
        "promedios": promedios,
        "desviaciones": desviaciones,
        "porcentajes_medios": porcentajes_medios,
        "ventas_promedio": ventas.mean(),
        "ventas_mediana": ventas.median(),
        "ventas_std": ventas.std(),
        "ventas_rango": ventas.max() - ventas.min(),
        "desperdicio_promedio": desperdicio.mean(),
        "desperdicio_mediana": desperdicio.median(),
        "desperdicio_std": desperdicio.std(),
        "desperdicio_rango": desperdicio.max() - desperdicio.min(),
        "porcentaje_desperdicio_promedio": porcentaje_desperdicio.mean(),
        "porcentaje_desperdicio": porcentaje_desperdicio,
    }


# ==============================
# Funciones para la GUI
# ==============================
def mostrar_resultados(metrics):
    resultados = f"""
    Promedio de Ventas por Trimestre y Total:
    {metrics["promedios"]}
    
    Desviación Estándar de Ventas por Trimestre y Total:
    {metrics["desviaciones"]}
    
    Porcentaje Promedio de Ventas de cada Trimestre respecto al Total:
    {metrics["porcentajes_medios"]}
    
    Estadísticas de Ventas:
    Promedio: {metrics["ventas_promedio"]}
    Mediana: {metrics["ventas_mediana"]}
    Desviación Estándar: {metrics["ventas_std"]}
    Rango: {metrics["ventas_rango"]}
    
    Estadísticas de Desperdicio:
    Promedio: {metrics["desperdicio_promedio"]}
    Mediana: {metrics["desperdicio_mediana"]}
    Desviación Estándar: {metrics["desperdicio_std"]}
    Rango: {metrics["desperdicio_rango"]}
    Promedio del Porcentaje de Desperdicio: {metrics["porcentaje_desperdicio_promedio"]}%
    """
    messagebox.showinfo("Resultados Estadísticos", resultados)


def graficar_distribucion(metrics, frame):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(metrics["porcentaje_desperdicio"], kde=True, color='purple', ax=ax)
    ax.set_title("Distribución del Porcentaje de Desperdicio")
    ax.set_xlabel("Porcentaje de Desperdicio")
    ax.set_ylabel("Frecuencia")

    canvas = FigureCanvasTkAgg(fig, frame)
    canvas.get_tk_widget().pack()
    canvas.draw()


# ==============================
# Configuración de la GUI
# ==============================
ventas_df, desperdicio_df = cargar_datos()
metrics = calcular_metricas(ventas_df, desperdicio_df) if ventas_df is not None else None

ventana = tk.Tk()
ventana.title("Proyecto Estadística")
ventana.geometry("800x600")

frame_grafico = tk.Frame(ventana)
frame_grafico.pack(fill="both", expand=True)

tk.Button(ventana, text="Mostrar Resultados", command=lambda: mostrar_resultados(metrics), bg="blue", fg="white").pack(pady=5)
tk.Button(ventana, text="Mostrar Gráfico", command=lambda: graficar_distribucion(metrics, frame_grafico), bg="green", fg="white").pack(pady=5)

ventana.mainloop()

