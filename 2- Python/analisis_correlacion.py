import os
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
import seaborn as sns


os.environ["PGCLIENTENCODING"] = "utf-8"

# 1) Configurar los parámetros de conexión
USUARIO = "postgres"
CONTRASENA = ""
HOST = "localhost"
PUERTO = "5432"
BASE_DATOS = "Supermarket Sales"


try:
    conn = psycopg2.connect(
        user=USUARIO,
        password=CONTRASENA,
        host=HOST,
        port=PUERTO,
        database=BASE_DATOS,
    )
    print("¡Conexión exitosa a 'Supermarket Sales' mediante psycopg2!")
except Exception as e:
    print(f"Error al conectar al servidor: {e}")
    exit()

# 2) Extraer los datos de la tabla principal
query = """
SELECT 
    precio_unitario, 
    cantidad, 
    "impuesto(5%)", 
    "venta_total(imp_inc)", 
    costo_de_venta, 
    beneficio_bruto, 
    "calificación"
FROM supermarket;
"""

try:
    df = pd.read_sql_query(query, conn)


    conn.close()

    print(f"Datos cargados con éxito. Filas detectadas: {len(df)}")


    df.columns = [
        "Precio Unitario",
        "Cantidad",
        "Impuesto (5%)",
        "Venta Total",
        "Costo de Venta",
        "Beneficio Bruto",
        "Calificación",
    ]

    # 3) Calcular la matriz de correlación de Pearson
    matriz_correlacion = df.corr(method="pearson")

    # 4) Configurar y generar el mapa de calor (Heatmap)
    plt.figure(figsize=(10, 8))

    sns.heatmap(
        matriz_correlacion,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",  
        linewidths=0.5,
        vmin=-1,
        vmax=1,
    )

    plt.title(
        "Matriz de Correlación de Pearson - Variables Numéricas",
        fontsize=14,
        pad=20,
    )
    plt.tight_layout()

    # 5) Guardar el gráfico en la carpeta del proyecto y mostrarlo
    plt.savefig("heatmap_correlacion.png", dpi=300)
    print(
        "¡ÉXITO! Gráfico guardado como 'heatmap_correlacion.png' en la carpeta de tu proyecto."
    )
    plt.show()

except Exception as e:
    print(f"Error al procesar la consulta o los datos: {e}")
    if "conn" in locals():
        conn.close()

