import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns
import csv, sqlite3

def fill_table(file_name, table_name, n_col):
    file = open(file_name, encoding="utf8")
    rows = csv.reader(file)
    next(file)
    insert_csv_to_table(table_name, n_col, rows)

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




def recomendar(usuario_id, pelicula_id):
    #movies = pd.read_csv("movies.csv")
    ratings = pd.read_csv("ratings.csv")
    hola = usuario_id
    adios = pelicula_id
    
    print(hola, adios)

    final_dataset = ratings.pivot(index='movieId',columns='userId',values='rating')
    final_dataset.fillna(0,inplace=True)
    #final_dataset.head()

    no_user_voted = ratings.groupby('movieId')['rating'].agg('count')
    no_movies_voted = ratings.groupby('userId')['rating'].agg('count')

    final_dataset = final_dataset.loc[no_user_voted[no_user_voted > 10].index,:]
    final_dataset=final_dataset.loc[:,no_movies_voted[no_movies_voted > 50].index]
    final_dataset

    #item based, voy por pelis
    peliculas = np.unique(ratings['movieId'])

    ratingmedia = df.ratings.groupby(["movieId"] ).mean().rename().rename(columns = {'rating': 'rating_media'})[['movieId','rating_media']]
    #columa de medias

    rating.merge(ratings, ratingmedia)

    ratings['rating_adjusted'] = ratings['rating']-ratings['rating_media']


if __name__ == "__main__":
    #fill_table('links.csv', 'links', 3)
    recomendar(0,1)