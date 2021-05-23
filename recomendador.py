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
    cursor.execute('SELECT userId FROM ratings WHERE movieId = ?', (pelicula,))
    resultado = cursor.fetchall()

    for [x] in resultado:
        var = str(x)
        usuarios.append(var)
    #print("*************************")
    #print(usuarios)

    return usuarios

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
    for [x] in resultado:
        var = str(x)
        pelisVistas.append(var)
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
    cursor.execute('SELECT rating FROM ratings WHERE userId = ?', str(usuario))
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

    for i in pelisVistas:
        pelicula = i
        #TODO PONER MOVIE ID, QUE LO HE QUITADO PARA VER SI FUNCIONA LA COMPARACION
        cur.execute('SELECT userId FROM ratings WHERE movieId = ?', (pelicula,))
        v1 = cur.fetchall()
        # TODO QUITAR FIXEO DE CORRECION DE COMAS:
        listaUsuarios.insert(i,pelicula)

        for [x] in v1:
            var = str(x)


            listaUsuarios.append(var)
        #listaUsuarios.append(arrayPuntual)
        listaVectores.append(listaUsuarios)
    print(listaUsuarios)
   # Lectura por consola del vector generado
    for a in listaVectores:
        # print(a)
        # print("\n")
        listaFinal.append(a)
   # print(listaFinal)
    return listaFinal


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



def similitudCoseno(listaCoincidencias, usuarios, posiciones, usuarioElegido):
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
    vectorInicial(144976)
    PelisVistasUsuarioSeleccionado(pelisVistas(610))
    #comparandoVectores(listaFinal, usuarios)
    #similitudCoseno(listaCoincidencias, usuarios, posiciones, 610)
    #ratingsUsuarioSeleccionado(1)




