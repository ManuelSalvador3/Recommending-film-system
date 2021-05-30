v1 = cur.fetchall()
        #TODO QUITAR FIXEO DE CORRECION DE COMAS:
        listaPelisNoVistas.insert(int(i), int(pelicula))

        for [x] in v1:
            var = str(x)
            listaUsuarios.insert(int(i), int(var))
        #listaUsuarios.append(arrayPuntual)
        listaVectores.append(listaUsuarios)
    print(listaUsuarios[0], listaUsuarios[7]) 
    #YA TENGO LAS DOS LISTAS
    

    # Lectura por consola del vector generado
    for a in listaVectores:
        # print(a)
        # print("\n")
        listaFinal.append(a)
   # print(listaFinal)




   listausuario = []
    x = 0
    for i in vectoresUsuarioRating:
        print(i)
        while x < len(i):
            if x%2 != 0:
                continue
            else:
                listausuario.append(vectoresUsuarioRating[x])
        print(listausuario)
        if i == 0 or int(i) % 2==0:
            continue
        else:
            hola = i
            print(hola)
            check = all(item in i for item in usuarios)
            if(check):
                listaCoincidencias.append(i)
                for l in enumerate(listaCoincidencias):
                    posiciones.append(l)











for y in vectortemporal:
                if z == 0 or z%2 ==0:
                    vectores.append(y)
                else: 
                    continue
                z+=1
        check = all(item in vectores for item in usuarios)
        if check:
            iguales.append(vectores)
            movies.append()
        x+=1
    print(iguales)