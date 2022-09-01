""" Creación de la base de datos y tabla """

import sqlite3

def crear_db():

    conexion = sqlite3.connect("tickers.db")

    cursor = conexion.cursor()

    try:
        cursor.execute("""
            CREATE TABLE tickers(
                nombre VARCHAR (10) PRIMARY KEY,
                fecha_inicio VARCHAR (10),
                fecha_fin VARCHAR (10),
                precio_apertura FLOAT (10),
                precio_cierre FLOAT (10),
                precio_mas_alto FLOAT (10),
                precio_mas_bajo FLOAT (10))""")

    except sqlite3.OperationalError:
        print("La tabla de tickers ya existe.")
    else:
        print("La tabla de tickers se ha creado correctamente.")

    conexion.close()

