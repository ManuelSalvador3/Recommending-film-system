import pandas as pd
import numpy as np
#from scipy.sparse import csr_matrix
#from sklearn.neighbors import NearestNeighbors
#import matplotlib.pyplot as plt
#import seaborn as sns
import csv, sqlite3
from scipy import spatial
import re

listaFinal = []
usuarios = []
listaCoincidencias = []
listaResultadosSC = []
posiciones = []
listaPelis = []
listaUsuarios = []
listaPelisNoVistas = []
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

def vectorInicial(pelicula):
    con = sqlite3.connect('movies.db')
    if con == None:
        print("Conexión no establecida'")
    else:
        print('Conexión establecida')

    cursor = con.cursor()
    cursor.execute('SELECT userId, rating FROM ratings WHERE movieId = ?', (pelicula,))
    resultado = cursor.fetchall()
    #Lo hacemos un especie de lista
    for row in resultado:
        usuarios.append(row[0])
        usuarios.append(row[1])
    print(usuarios)
    return usuarios #Todos los usuarios que han visto la peli el bucle debe ir de 2 en 2 para coger todo 

#Pelicules que ha visto el usuario seleccionado
def pelisVistas(usuario):
    con = sqlite3.connect('movies.db')
    if con == None:
        print("Conexión no establecida'")
    else:
        print('Conexión establecida')
    cursor = con.cursor()
    cursor.execute('SELECT movieId FROM ratings WHERE userId = ?', (usuario,))
    resultado = cursor.fetchall()
    pelisVistas = []
    for row in resultado:
        pelisVistas.append(row[0])
    #print(pelisVistas)
    #print(pelisVistas)
    cursor.close()
    con.close()
    return pelisVistas
#Ratings de las pelis que ha visto el usuario, para calcular la similitud del coseno
def ratingsUsuarioSeleccionado(usuario):
    con = sqlite3.connect('movies.db')
    if con == None:
        print("Conexión no establecida")
    else:
        print("Conexión establecida")

    cursor = con.cursor()
    cursor.execute('SELECT rating FROM ratings WHERE userId = ?', (usuario,))
    resultado = cursor.fetchall()
    ratingsUsuario = []
    for [x] in resultado:
        var = str(x)
        ratingsUsuario.append(var)
    #print(ratingsUsuario)

    cursor.close()
    con.close()
    return ratingsUsuario



#Lista de vectores de los ratings de las peliculas que ha visto el usuario seleccionado
def PelisVistasUsuarioSeleccionado(pelisVistas):
    listaVectores = []
    con = sqlite3.connect('movies.db')
    if con == None:
        print("Conexión no establecida")
    else:
        print('Conexión establecida')
    # FUNCION DONDE VAMOS HACER LA PREDICCION DE LA PELICULA
    cur = con.cursor()
    # Primer vector donde cogemos todos los ratings de la peli que queremos
    userid_rating = []
    vectores_movies_users = []
    for i in pelisVistas:
        pelicula = i
        vectores_movies_users.append(pelicula)
        #TODO PONER MOVIE ID, QUE LO HE QUITADO PARA VER SI FUNCIONA LA COMPARACION
        cur.execute('SELECT userId, rating FROM ratings WHERE movieId = ?', (pelicula,))
        resultado = cur.fetchall()
        for row in resultado:
            userid_rating.append(row[0])
            userid_rating.append(row[1])
        

    return "gola"

def comparandoVectores(listaFinal, usuarios):
    for i in listaFinal:
        check = all(item in i for item in usuarios)
        if(check):
            listaCoincidencias.append(i)
            for l in enumerate(listaCoincidencias):
                posiciones.append(l)
    #print(posiciones)




       # print(check)
    # for i in listaCoincidencias:
    #     print(i)
    #print(usuarios)
    return listaCoincidencias, posiciones



def similitudCoseno(listaCoincidencias, usuarios, usuarioElegido):
    con = sqlite3.connect('movies.db')
    if con == None:
        print("Conexión no establecida")
    else:
        print("Conexión establecida")


    cursor = con.cursor()
    cursor.execute('SELECT rating FROM ratings WHERE userId = ?', (usuarioElegido,))
    result = cursor.fetchall()

    for [x] in result:
        var = str(x)
        listaPelis.append(var)
    cursor.close()
    con.close()

    # for j in posiciones:
    #     print(j)
        #pelisVistas = listaPelis[posiciones[j]]
    # for i in listaCoincidencias:
    #     #Formula Similitud entre
    #     #print(i)
    #     result = 1 - spatial.distance.cosine(i,usuarios)
    #     listaResultadosSC.append(result)
    #print(listaResultadosSC)




if __name__ == "__main__":
    #fill_table('links.csv', 'links', 3)
    #pelisVistas(1)
    #vectorInicial(2)
    PelisVistasUsuarioSeleccionado(pelisVistas(vectorInicial(2)))
    #comparandoVectores(listaFinal, usuarios)
    #similitudCoseno(listaCoincidencias, usuarios, posiciones, 610)
    #ratingsUsuarioSeleccionado(1)




