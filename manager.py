""" Funciones del programa """

import helpers
import requests
import json
import sqlite3
import re

def ticker():

    ticker = input(">>> Ingrese ticker a pedir:\n")

    while True:

        fecha_inicio = input(">>> Ingrese fecha de inicio (formato YYYY-MM-DD):\n")

        if re.match("[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha_inicio) and len(fecha_inicio) == 10:
            break
        print("Formato de fecha incorrecto")

    while True:

        fecha_fin = input(">>> Ingrese fecha de fin (formato YYYY-MM-DD):\n")

        if re.match("[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha_fin) and len(fecha_fin) == 10:
            break
        print("Formato de fecha incorrecto")

    print("Pidiendo datos...")

    res = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{fecha_inicio}/{fecha_fin}?adjusted=true&sort=asc&limit=120&apiKey=_i0PIv435ie2k6p6Oc6rT162DokO4cO6")
    
    data = res.json()
    print(data)
    precio_apertura = data["results"][0]["o"]
    precio_cierre = data["results"][-1]["c"]

    precio_mas_alto = data["results"][0]["o"]
    precio_mas_bajo = data["results"][-1]["c"]

    for valores in data["results"]:
        if valores["h"] >= precio_mas_alto:
            precio_mas_alto = valores["h"]
        if valores["l"] <= precio_mas_bajo:
            precio_mas_bajo = valores["l"]
    
    datos_a_cargar = (ticker,fecha_inicio,fecha_fin,precio_apertura,precio_cierre,precio_mas_alto,precio_mas_bajo)

    guardar_datos_db(datos_a_cargar)

def guardar_datos_db(valores):

    conexion = sqlite3.connect("tickers.db")
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO tickers VALUES (?,?,?,?,?,?,?)", valores)

    conexion.commit()
    conexion.close()

    print("Datos guardados correctamente")

def resumen_db():

    conexion = sqlite3.connect("tickers.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM tickers")

    tickers = cursor.fetchall()

    print("Los tickers guardados en la base de datos son:")

    for ticker in tickers:
        print(f"{ticker[0]:4} - {ticker[1]} <-> {ticker[2]}")

    conexion.close()