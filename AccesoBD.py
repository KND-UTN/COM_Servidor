import sqlite3 as sql
import pathlib


def ejecutar(query):
    conexion = sql.connect(str(pathlib.Path(__file__).parent.absolute()) + '\\bd.db')
    ejecutador = conexion.cursor()
    ejecutador.execute(query)
    conexion.commit()


def ejecutar_parametros(query, parametros):
    conexion = sql.connect(str(pathlib.Path(__file__).parent.absolute()) + '\\bd.db')
    ejecutador = conexion.cursor()
    ejecutador.execute(query, parametros)
    conexion.commit()


def leer(query):
    conexion = sql.connect(str(pathlib.Path(__file__).parent.absolute()) + '\\bd.db')
    ejecutador = conexion.cursor()
    ejecutador.execute(query)
    return ejecutador.fetchall()


def leer_parametros(query, parametros):
    conexion = sql.connect(str(pathlib.Path(__file__).parent.absolute()) + '\\bd.db')
    ejecutador = conexion.cursor()
    ejecutador.execute(query, parametros)
    return ejecutador.fetchall()