import pandas as pd
import tkinter as tk
from tkinter import messagebox


# ==============================
# Función para cargar datos
# ==============================
def cargar_datos():
    try:
        # Cargar ventas
        file_path_ventas = 'Desarrollo/datos Informe de ventas Pan & Arte Yumbo.xlsx'
        ventas_df = pd.read_excel(file_path_ventas, sheet_name='Datos de ventas', skiprows=1)

        # Cargar desperdicios (causas de devolución)
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
    }


# ==============================
# Función para mostrar resultados
# ==============================
def mostrar_resultados(metrics):
    resultados = f"""
    ====================================
             RESULTADOS ESTADÍSTICOS
    ====================================

    PROMEDIOS DE VENTAS POR TRIMESTRE:
        1er Trimestre:    {metrics["promedios"]["1er_trim"]:.2f}
        2do Trimestre:    {metrics["promedios"]["2do_trim"]:.2f}
        3er Trimestre:    {metrics["promedios"]["3er_trim"]:.2f}
        4to Trimestre:    {metrics["promedios"]["4to_trim"]:.2f}
        Total:            {metrics["promedios"]["Total"]:.2f}

    DESVIACIÓN ESTÁNDAR DE VENTAS POR TRIMESTRE:
        1er Trimestre:    {metrics["desviaciones"]["1er_trim"]:.2f}
        2do Trimestre:    {metrics["desviaciones"]["2do_trim"]:.2f}
        3er Trimestre:    {metrics["desviaciones"]["3er_trim"]:.2f}
        4to Trimestre:    {metrics["desviaciones"]["4to_trim"]:.2f}
        Total:            {metrics["desviaciones"]["Total"]:.2f}

    PORCENTAJE PROMEDIO DE VENTAS POR TRIMESTRE RESPECTO AL TOTAL:
        1er Trimestre:    {metrics["porcentajes_medios"]["1er_trim"]:.2f}%
        2do Trimestre:    {metrics["porcentajes_medios"]["2do_trim"]:.2f}%
        3er Trimestre:    {metrics["porcentajes_medios"]["3er_trim"]:.2f}%
        4to Trimestre:    {metrics["porcentajes_medios"]["4to_trim"]:.2f}%

    ====================================
               ESTADÍSTICAS GLOBALES
    ====================================

    ESTADÍSTICAS DE VENTAS:
        Promedio:         {metrics["ventas_promedio"]:.2f}
        Mediana:          {metrics["ventas_mediana"]:.2f}
        Desviación Std.:  {metrics["ventas_std"]:.2f}
        Rango:            {metrics["ventas_rango"]:.2f}

    ESTADÍSTICAS DE DESPERDICIO:
        Promedio:         {metrics["desperdicio_promedio"]:.2f}
        Mediana:          {metrics["desperdicio_mediana"]:.2f}
        Desviación Std.:  {metrics["desperdicio_std"]:.2f}
        Rango:            {metrics["desperdicio_rango"]:.2f}

    PORCENTAJE PROMEDIO DE DESPERDICIO:
        {metrics["porcentaje_desperdicio_promedio"]:.2f}%

    ====================================
    """
    text_resultados.delete("1.0", tk.END)  # Limpiar el cuadro de texto
    text_resultados.insert(tk.END, resultados)  # Mostrar los resultados


# ==============================
# Configuración de la GUI
# ==============================
ventas_df, desperdicio_df = cargar_datos()
metrics = calcular_metricas(ventas_df, desperdicio_df) if ventas_df is not None else None

ventana = tk.Tk()
ventana.title("Proyecto Estadística")
ventana.geometry("800x600")

# Cuadro de texto para mostrar resultados
text_resultados = tk.Text(ventana, wrap="word", font=("Courier New", 12), bg="white", fg="black")
text_resultados.pack(expand=True, fill="both", padx=10, pady=10)

if metrics:
    mostrar_resultados(metrics)

ventana.mainloop()
