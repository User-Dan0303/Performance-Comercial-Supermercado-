import os
import pandas as pd
import psycopg2

# Forzar a Windows a usar UTF-8 para evitar errores de caracteres
os.environ["PGCLIENTENCODING"] = "utf-8"

# 1. Parámetros de conexión a tu PostgreSQL
USUARIO = "postgres"
CONTRASENA = "cabozero22"  # <-- Coloca aquí tu clave
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
    print("¡Conexión exitosa para extracción de vistas!")
except Exception as e:
    print(f"Error al conectar: {e}")
    exit()

# 2. Diccionario con las vistas de PostgreSQL y el nombre que tendrán las pestañas en Excel
vistas_a_exportar = {
    "Rentabilidad": "vista_rentabilidad_segmentada",
    "Ticket Promedio": "vista_ticket_promedio",
    "Análisis Temporal": "vista_analisis_temporal_pagos",
    "Franjas Horarias": "vista_ventas_por_franja_horaria",
}

nombre_archivo_excel = "Reporte_Control_Financiero.xlsx"

try:
    # Usamos ExcelWriter de Pandas para escribir múltiples pestañas en un solo archivo
    with pd.ExcelWriter(nombre_archivo_excel, engine="openpyxl") as writer:

        for nombre_pestaña, nombre_vista in vistas_a_exportar.items():
            query = f'SELECT * FROM "{nombre_vista}";'

            # Leemos la vista desde la base de datos
            df_vista = pd.read_sql_query(query, conn)

            # Exportamos el DataFrame a su respectiva pestaña de Excel
            df_vista.to_excel(writer, sheet_name=nombre_pestaña, index=False)
            print(
                f"-> Vista '{nombre_vista}' exportada con éxito a la pestaña '{nombre_pestaña}'."
            )

    print("\n========================================================")
    print(
        f"¡ÉXITO TOTAL! El archivo '{nombre_archivo_excel}' ha sido generado."
    )
    print(
        "Se encuentra guardado en la carpeta de tu proyecto de PyCharm."
    )
    print("========================================================")

except Exception as e:
    print(f"Error durante el proceso de automatización: {e}")

finally:
    # Cerramos la conexión de forma segura
    if "conn" in locals():
        conn.close()
