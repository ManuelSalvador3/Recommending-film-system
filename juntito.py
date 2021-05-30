import pandas as pd
import numpy as np
#from scipy.sparse import csr_matrix
#from sklearn.neighbors import NearestNeighbors
#import matplotlib.pyplot as plt
#import seaborn as sns
import csv, sqlite3
from scipy import spatial
import re


def predecir(self, usuario, pelicula):
        con = sqlite3.connect('movies.db')
        if con == None:
            print("Conexión no establecida'")
        else:
            print('Conexión establecida')
        cursor = con.cursor()
        self.usuario = str(self.comboBox_Usuario2.currentText())
        self.pelicula =str(self.comboBox_Pelicula.currentText())
        print(usuario, pelicula)
        print("Llego")
        self.cursor.execute('SELECT userId, rating FROM ratings WHERE movieId = ?', (pelicula,))
        resultado = self.cursor.fetchall()
        usuarios = [] #usuarios que han rateado la peli a predecir
        #Lo hacemos un especie de lista
        for row in resultado: 
            usuarios.append(row[0])
            usuarios.append(row[1])
        #usuarios es el vector inicial
        print(usuarios)
        #Query para ver las peliculas que ha visto el usuario
        self.cursor.execute('SELECT movieId FROM ratings WHERE userId = ?', (usuario,))
        resultado = self.cursor.fetchall()
        pelisVistas = []
        for row in resultado:
            pelisVistas.append(row[0])
        #pelisVistas son todas las peliculas que ha visto el usuario
        print(pelisVistas)
        vectoresUsuarioRating = []
        #Vector de pelis vistas por el usuario
        for i in pelisVistas:
            pelicula = i
            userid_vectores = [] #Almacena los ususarios id de todos los vectores
            #Sacamos todos los usuarios que han dado rating a cada pelio que ha visto el usuario
            self.cursor.execute('SELECT userId FROM ratings WHERE movieId = ?', (pelicula,))
            resultado = self.cursor.fetchall()
            for row in resultado:
                userid_vectores.append(row[0]) #Insertamos userId
                #userid_rating.append(row[1]) #Rating que le ha dado el usuario
            vectoresUsuarioRating.append(userid_vectores) #Solo los usersID y 
        print(vectoresUsuarioRating) #Todos los vectores de usuarios
        iguales = []
        ordenPelisVistas = []
        x =0 
        for i in vectoresUsuarioRating: #peli [usuario, rating.....], peli......
            check = all(item in vectoresUsuarioRating for item in usuarios)
            if check:
                iguales.append(vectoresUsuarioRating)
                ordenPelisVistas.append(x)
                x+=1
            else:
                print('Error no son iguales el vector con el vector original')
                x+=1
        
        if len(iguales) == 0:
            self.resultado_prediccion.setText('Error :(')
            print('No se ha encontrado ningun vector que coincida con el vector original')
        else:
            print(iguales)

        #Cuando ya tenemos los vectores iguales
        return iguales

if __name__ == "__main__":
    predecir(1, 318)
