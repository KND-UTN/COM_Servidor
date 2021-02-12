_author_ = "Ignacio Pieve Roiger"
_version_ = "0.1"


# En este script lo unico que se hace es crear la base de datos
# y llenarla de todos los datos basicos como los nombres de las materias, sus correlatividades, etc

import AccesoBD as bd
import os
import pathlib


# Este metodo checkea si la base de datos existe, y si no la crea vacia y la llena con los datos basicos
# Se ejecuta al inicio del programa
def checkearCrearLlenar():
    if not os.path.isfile(str(pathlib.Path(__file__).parent.absolute()) + '\\bd.db'):
        print('Inicializando base de datos por primera vez, por favor espere...')
        crear_base()
        llenar_materias()
        llenar_correlatividades()
        print('Bienvenido, se ha creado una nueva base de datos.\nRecuerda llenar los datos de las materias y tu usuario de autogestion.\n\n')


def crear_base():
    try:
        bd.ejecutar('''CREATE TABLE "Aprobaciones" (
                    "idMateria"	INTEGER,
                    "fecha"	TEXT,
                    "nota"	INTEGER CHECK("nota" <= 10),
                    FOREIGN KEY("idMateria") REFERENCES "Materias"("id")
                );''')
        bd.ejecutar('''CREATE TABLE "Correlativ.Cursar.Aprov" (
                    "idCorrelatividad"	INTEGER,
                    "idMateria"	INTEGER,
                    "idMateriaNecesaria"	INTEGER,
                    PRIMARY KEY("idCorrelatividad" AUTOINCREMENT),
                    FOREIGN KEY("idMateria") REFERENCES "Materias"("id"),
                    FOREIGN KEY("idMateriaNecesaria") REFERENCES "Materias"("id")
                );''')
        bd.ejecutar('''CREATE TABLE "Correlativ.Cursar.Regular" (
                    "idCorrelatividad"	INTEGER,
                    "idMateria"	INTEGER,
                    "idMateriaNecesaria"	INTEGER,
                    FOREIGN KEY("idMateriaNecesaria") REFERENCES "Materias"("id"),
                    FOREIGN KEY("idMateria") REFERENCES "Materias"("id"),
                    PRIMARY KEY("idCorrelatividad" AUTOINCREMENT)
                );''')
        bd.ejecutar('''CREATE TABLE "Correlativ.Rendir.Aprov" (
                    "idCorrelatividad"	INTEGER,
                    "idMateria"	INTEGER,
                    "idMateriaNecesaria"	INTEGER,
                    FOREIGN KEY("idMateria") REFERENCES "Materias"("id"),
                    FOREIGN KEY("idMateriaNecesaria") REFERENCES "Materias"("id"),
                    PRIMARY KEY("idCorrelatividad" AUTOINCREMENT)
                );''')
        bd.ejecutar('''CREATE TABLE "Materias" (
                    "id"	INTEGER,
                    "abreviacion"	TEXT,
                    "nombre"	TEXT,
                    "horasSemanales"	REAL,
                    "tipo"	INTEGER,
                    "nivel"	INTEGER,
                    PRIMARY KEY("id")
                );''')
        bd.ejecutar('''CREATE TABLE "Regularidades" (
                    "idMateria"	INTEGER,
                    "startYear"	INTEGER,
                    "startCuatrimestre"	INTEGER,
                    "curso"	INTEGER,
                    "estado"	TEXT,
                    "uvlink"	TEXT,
                    FOREIGN KEY("idMateria") REFERENCES "Materias"("id"),
                    PRIMARY KEY("idMateria")
                );''')
        bd.ejecutar('''CREATE TABLE "Notas" (
                    "idMateria"	INTEGER,
                    "descripcion"	TEXT,
                    "nota"	TEXT
                );''')
        bd.ejecutar('''CREATE TABLE "Chequeos" (
                    "idMateria"	INTEGER,
                    "ultimoIntento"	TEXT,
                    "ultimoCorrecto"	TEXT,
                    "ultimoError"	TEXT,
                    PRIMARY KEY("idMateria")
                );''')
        bd.ejecutar('''CREATE TABLE "Usuario" (
                    "usuario"	TEXT,
                    "clave"	TEXT,
                    PRIMARY KEY("usuario")
                );''')
        bd.ejecutar('''CREATE TABLE "Mensajes" (
                    "fecha"	TEXT,
                    "curso"	TEXT,
                    "profesor"	TEXT,
                    "mensaje"	TEXT
                );''')
        bd.ejecutar('''CREATE TABLE "token_slack" (
                    "token"	TEXT
                );''')
    except:
        print("Ya existe una base de datos.")


def llenar_materias():
    try:
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (1, "AMI", "Analisis Matemático I", 5, "Anual", 1);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (2, "AGA", "Algebra y Geometría Analítica", 5, "Anual", 1);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (3, "MAD", "Matemática Discreta", 6, "Cuatrimestral", 1);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (4, "SOR", "Sistemas y Organizaciones", 6, "Cuatrimestral", 1);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (5, "AED", "Algoritmos y Estructuras de Datos", 5, "Anual", 1);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (6, "ACO", "Arquitectura de Computadoras", 8, "Cuatrimestral", 1);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (7, "FIS", "Física I", 5, "Anual", 1);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (8, "ING", "Inglés", 2, "Anual", 1);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (22, "ISI", "Ingeniería y Sociedad", 4, "Cuatrimestral", 1);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (9, "QUI", "Química", 6, "Cuatrimestral", 2);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (10, "AMII", "Analisis Matemático II", 5, "Anual", 2);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (11, "FISII", "Física II", 5, "Anual", 2);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (12, "ASI", "Análisis de Sistemas", 6, "Anual", 2);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (13, "SSL", "Sintaxis y Semántica de los Lenguajes", 8, "Cuatrimestral", 2);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (14, "PPR", "Paradigmas de Programación", 8, "Cuatrimestral", 2);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (15, "SOP", "Sistemas Operativos", 4, "Anual", 2);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (17, "PYE", "Probabilidad y Estadística", 6, "Cuatrimestral", 2);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (16, "SSR", "Sistemas de Representación", 3, "Anual", 3);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (18, "DSI", "Diseño de Sistemas", 6, "Anual", 3);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (19, "COM", "Comunicaciones", 4, "Anual", 3);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (20, "MAS", "Matemática Superior", 8, "Cuatrimestral", 3);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (21, "GDA", "Gestión de Datos", 8, "Cuatrimestral", 3);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (23, "ECO", "Economía", 6, "Cuatrimestral", 3);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (24, "INGII", "Inglés II", 2, "Anual", 3);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (25, "RIN", "Redes de Información", 4, "Anual", 4);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (26, "ARE", "Administración de Recursos", 6, "Anual", 4);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (27, "IOP", "Investigación Operativa", 5, "Anual", 4);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (28, "SIM", "Simulación", 8, "Cuatrimestral", 4);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (29, "ISW", "Ingeniería de Software", 6, "Cuatrimestral", 4);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (30, "TCO", "Teoría de Control", 6, "Cuatrimestral", 4);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (31, "LEG", "Legislación", 4, "Cuatrimestral", 4);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (32, "PF", "Proyecto Final", 6, "Anual", 5);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (33, "IA", "Inteligencia Artificial", 3, "Anual", 5);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (34, "AGE", "Administración General", 6, "Cuatrimestral", 5);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (35, "SGO", "Sistemas de Gestión", 4, "Anual", 5);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (101, "PAVI", "Programación de Aplicaciones Visuales I", 8, "Electiva", 0);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (102, "PAVII", "Programación de Aplicaciones Visuales II", 8, "Electiva", 0);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (103, "TSB", "Tecnología de Software de Base", 8, "Electiva", 0);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (104, "DLC", "Diseño de Lenguaje de Consulta", 8, "Electiva", 0);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (105, "GMP", "Gestión de la Mejora de los Procesos", 6, "Electiva", 0);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (106, "TED", "Tecnología Educativa", 6, "Electiva", 0);')
        bd.ejecutar(
            'INSERT INTO "Materias" (id, abreviacion, nombre, horasSemanales, tipo, nivel) VALUES (107, "GIP", "Gestión Industrial de la Producción", 6, "Electiva", 0);')
    except:
        print('Error llenando las materias.')


def llenar_correlatividades():
    try:
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (10, 1);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (10, 2);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (11, 1);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (11, 7);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (12, 4);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (12, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (13, 3);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (13, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (14, 3);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (14, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (15, 3);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (15, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (15, 6);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (17, 1);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (17, 2);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (18, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (18, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (19, 6);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (19, 10);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (19, 11);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (20, 10);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (21, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (21, 13);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (21, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (23, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (25, 15);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (25, 19);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (26, 15);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (26, 18);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (26, 23);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (27, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (27, 20);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (28, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (28, 20);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (29, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (29, 18);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (29, 21);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (30, 9);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (30, 20);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (31, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (31, 22);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (32, 25);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (32, 26);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (32, 29);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (32, 31);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (33, 27);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (33, 28);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (34, 26);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (34, 27);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (35, 26);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (35, 27);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (35, 28);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (101, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (101, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (102, 101);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (103, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (104, 103);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (105, 4);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (105, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (106, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Regular" (idMateria, idMateriaNecesaria)VALUES (107, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (18, 3);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (18, 4);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (18, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (19, 1);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (19, 2);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (19, 7);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (20, 1);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (20, 2);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (21, 3);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (21, 4);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (21, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (23, 4);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (23, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (24, 8);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (25, 3);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (25, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (25, 6);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (25, 10);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (25, 11);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (26, 6);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (26, 8);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (26, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (26, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (27, 10);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (28, 10);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (29, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (29, 13);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (29, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (30, 10);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (30, 11);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (31, 4);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (31, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 15);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 16);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 18);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 19);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 21);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 22);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 23);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 24);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (33, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (33, 18);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (33, 20);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (34, 15);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (34, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (34, 18);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (34, 20);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (34, 23);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (35, 15);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (35, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (35, 18);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (35, 20);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (35, 23);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (102, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (103, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (106, 4);')
        bd.ejecutar('INSERT INTO "Correlativ.Cursar.Aprov" (idMateria, idMateriaNecesaria)VALUES (107, 4);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (10, 1);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (10, 2);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (11, 1);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (11, 7);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (12, 4);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (12, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (13, 3);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (13, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (14, 3);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (14, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (15, 3);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (15, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (15, 6);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (17, 1);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (17, 2);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (18, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (18, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (19, 6);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (19, 10);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (19, 11);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (20, 10);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (21, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (23, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (25, 15);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (25, 19);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (26, 15);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (26, 18);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (26, 23);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (27, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (27, 20);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (28, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (28, 20);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (29, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (29, 18);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (29, 21);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (30, 9);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (30, 20);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (31, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (31, 22);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 1);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 2);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 3);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 4);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 6);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 7);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 8);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 9);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 10);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 11);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 12);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 13);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 15);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 16);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 17);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 18);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 19);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 20);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 21);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 22);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 23);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 24);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 25);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 26);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 27);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 28);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 29);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 30);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 31);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 33);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 34);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (32, 35);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (33, 27);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (33, 28);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (34, 26);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (34, 27);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (35, 26);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (35, 27);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (35, 28);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (101, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (101, 5);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (103, 14);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (104, 103);')
        bd.ejecutar('INSERT INTO "Correlativ.Rendir.Aprov" (idMateria, idMateriaNecesaria)VALUES (105, 12);')
    except:
        print('Error llenando las correlatividades.')



if __name__ == "__main__":
    crear_base()
    #checkearCrearLlenar()