import pandas as pd
import numpy as np
#from scipy.sparse import csr_matrix
#from sklearn.neighbors import NearestNeighbors
#import matplotlib.pyplot as plt
#import seaborn as sns
import csv, sqlite3
import re

#LLENAMOS LA TABLA
def fill_table(file_name, table_name, n_col):
    file = open(file_name, encoding="utf8")
    rows = csv.reader(file)
    next(file)
    insert_csv_to_table(table_name, n_col, rows)

#INSERTAMOS EN LA BASE DE DATOS
def insert_csv_to_table(table_name, n_col, rows):
    con = sqlite3.connect('movies.db')
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM " + table_name)
    result = cur.fetchall()
    values = ""
    i = 0
    for i in range(n_col):
        values = values + "?,"
    values = values[:-1]
    if result[0][0] == 0:
        cur.executemany("INSERT OR IGNORE INTO " + table_name + " VALUES ("+ values + ")", rows)
    con.commit()
    con.close()

#Pelicules que ha visto el usuario seleccionado
def pelisVistas(usuario):
    con = sqlite3.connect('movies.db')
    if con == None:
        print("Hola")
    else:
        print('Funciona')

    cursor = con.cursor()
    cursor.execute('SELECT movieId FROM ratings WHERE userId = ?', str(usuario))
    resultado = cursor.fetchall()
    pelisVistas = []
    for [x] in resultado:
        var = str(x)
        pelisVistas.append(var)
    print(pelisVistas)  

    #print(pelisVistas)
    cursor.close()
    con.close()
    return pelisVistas

#Ratings de las pelis que ha visto el usuario, para calcular la similitud del coseno
def RatingPelis(pelisVistas):
    con = sqlite3.connect('movies.db')
    if con == None:
        print("Conexion establecida RatingPelis")
    else:
        print('Funciona')
    # FUNCION DONDE VAMOS HACER LA PREDICCION DE LA PELICULA
    cur = con.cursor()
    # Primer vector donde cogemos todos los ratings de la peli que queremos
    for i in pelisVistas:
        pelicula = i
        cur.execute('SELECT userId, rating FROM ratings WHERE movieId = ?', (pelicula,))
        v1 = cur.fetchall()
        print("Para la pelicula con id: " + i)
        print(v1)

        print('\n')



if __name__ == "__main__":
    #fill_table('links.csv', 'links', 3)
    #pelisVistas(1)
    RatingPelis(pelisVistas(1))

