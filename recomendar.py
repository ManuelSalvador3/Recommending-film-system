def recomendar(self):
        ranking = self.Items_ranking_textEdit.toPlainText()
        usuario = str(self.comboBox_Usuario1.currentText())
        umbral = self.umbral_similitud_textEdit.toPlainText()
        
        print(usuario, ranking, umbral)
        #Insertamos las filas necesarias
        x = 0
        self.tableWidget.clear()
        while x < int(ranking): #Funciona
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            x+=1
     
        pelisVistas = [] #Pelis que ha visto el usuario
        self.cursor.execute('SELECT movieId FROM ratings WHERE userId = ?', (usuario,)) #Todas las pelis que ha visto el usuario las cuales podemos reocmendar
        result = self.cursor.fetchall()
        for row in result:
            pelisVistas.append(row[0])
        #print(pelisVistas) #FUNCIONA
        
        #Pelis que no ha visto el usuario
        self.cursor.execute('SELECT DISTINCT movieId FROM movies WHERE movieId not in (SELECT movieId from ratings WHERE userId = ?)', (usuario,))
        result = self.cursor.fetchall()
        pelisNoVistas = []
        for row in result:
            pelisNoVistas.append(row[0])
        #print(pelisNoVistas) #Funciona
        for x in pelisNoVistas: #Por cada peli que el usuario no ha visto
            vector_inicial = []
            print("Nueva peli")
            self.cursor.execute('SELECT userId FROM ratings WHERE movieId = ?', (x,)) #Vector de la peli
            resultado = self.cursor.fetchall()
            for row in resultado:
                vector_inicial.append(row[0]) #usuario que han rateado la primera peli
            #print(vector_inicial) #Printea el vector incicial de todas las pelis
            #Ya tengo el vector inicial, ahora sacar todos los vectores del resto de las pelis
            #Sacar el vector del resto de las pelis vistas
            vectoresUsuarioRating = []
            for y in pelisVistas:
                userid_vectores = [] #Almacena los ususarios id de todos los vectores
                #Sacamos todos los usuarios que han dado rating a cada pelio que ha visto el usuario
                self.cursor.execute('SELECT userId FROM ratings WHERE movieId = ?', (y,))
                resultado = self.cursor.fetchall()
                for row in resultado:
                    userid_vectores.append(row[0]) #Insertamos userId
                vectoresUsuarioRating.append(userid_vectores) #FUNCIONA CORRECTAMENTE
                #Ya tengo todos los vectores
                iguales = []
                ordenPelisVistas = []
                z =0 
                for i in vectoresUsuarioRating: 
                    vectortemporal = i
                    #print(vectortemporal)
                    #peli [usuario, rating.....], peli......
                    #print(vectortemporal)
                    check = all(item in vectortemporal for item in vector_inicial)
                    if check:
                        usuarios_iguales = set(vectortemporal).intersection(vector_inicial)
                        vector = list(usuarios_iguales)
                        #print(vector, type(vector))
                        iguales.append(vector)
                        ordenPelisVistas.append(pelisVistas[x])
                        z+=1
                    else:
                        z+=1
                if len(iguales) == 0:
                    print("Esta peli no tiene vectores iguales")
                    #break #print('No se ha encontrado ningun vector que coincida con el vector original')
                else:
                    #print("Ha funcionado")
                    pelis_coseno = []
                    y = 0
                    for vector in iguales: 
                        #Funciona
                        similitud = 1 - spatial.distance.cosine(vector, vector_inicial)    
                        if similitud >= umbral:
                            pelis_coseno.append(ordenPelisVistas[z])
                            y+=1
                        else:
                            y +=1
                    #print("Hola")
                    numerador = 0 
                    denominador = 0
                    peli_rating = []
                    lista_predicciones = []
                    for i in pelis_coseno:
                        #Da mal la consulta
                        self.cursor.execute('SELECT rating FROM ratings WHERE userId = ?1 AND movieId = ?2', (usuario, i,))
                        resultado = self.cursor.fetchall()
                        for row in resultado:
                            ratings_usuario = row[0]
                        #print(ratings_usuario)
                        numerador += ratings_usuario
                        denominador +=1
                    prediccion = numerador/denominador 
                    #print(prediccion)
                    lista_predicciones.append(prediccion) #Me guardo todas las predicciones realizadas
                    peli_rating.append(x)
                    #print(lista_predicciones)
            print(lista_predicciones)
            #Comparar todos los ratings 