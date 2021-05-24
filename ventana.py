# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from scipy import spatial
import sys
import random 
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_MainWindow(object):
    def __init__(self):
        self.con = sqlite3.connect('movies.db')
        if self.con == None:
            print("Hola")
        else:
            print('Funciona')
        self.cursor = self.con.cursor()

    def setupUi(self, MainWindow):
        self.cursor.execute('SELECT userId FROM ratings GROUP BY userId')
        resultado = self.cursor.fetchall()
        Usuarios = []
        for [x] in resultado:
            var = str(x)
            Usuarios.append(var)
        #print(Usuarios)


        #self.cursor.execute('SELECT userId FROM ratings GROUP BY userId')
        #resultado = self.cursor.fetchall()
        #for x in 610:
            #self.cursor.execute('SELECT movieId FROM ratings WHERE userId != ?', x)
            #result = self.cursor.fetchall()
            #pelisNoVistas = []
        #for [x] in result:
            #var = str(x)
            #pelisNoVistas.append(var)


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 606)
        font = QtGui.QFont()
        font.setUnderline(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Recomendar_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Recomendar_Button.setGeometry(QtCore.QRect(620, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Recomendar_Button.setFont(font)
        self.Recomendar_Button.setObjectName("Recomendar_Button")
        self.Predecir_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Predecir_Button.setGeometry(QtCore.QRect(630, 490, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Predecir_Button.setFont(font)
        self.Predecir_Button.setObjectName("Predecir_Button")
        self.horizontal_line = QtWidgets.QFrame(self.centralwidget)
        self.horizontal_line.setGeometry(QtCore.QRect(0, 410, 851, 16))
        self.horizontal_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontal_line.setObjectName("horizontal_line")
        self.recomendaciones_label = QtWidgets.QLabel(self.centralwidget)
        self.recomendaciones_label.setGeometry(QtCore.QRect(40, 10, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.recomendaciones_label.setFont(font)
        self.recomendaciones_label.setObjectName("recomendaciones_label")
        self.items_ranking_label = QtWidgets.QLabel(self.centralwidget)
        self.items_ranking_label.setGeometry(QtCore.QRect(40, 100, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.items_ranking_label.setFont(font)
        self.items_ranking_label.setObjectName("items_ranking_label")
        self.selecciona_usuario_label = QtWidgets.QLabel(self.centralwidget)
        self.selecciona_usuario_label.setGeometry(QtCore.QRect(40, 60, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.selecciona_usuario_label.setFont(font)
        self.selecciona_usuario_label.setObjectName("selecciona_usuario_label")
        self.selecciona_usuario_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.selecciona_usuario_label_2.setGeometry(QtCore.QRect(40, 440, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.selecciona_usuario_label_2.setFont(font)
        self.selecciona_usuario_label_2.setObjectName("selecciona_usuario_label_2")
        self.selecciona_peli_label = QtWidgets.QLabel(self.centralwidget)
        self.selecciona_peli_label.setGeometry(QtCore.QRect(40, 490, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.selecciona_peli_label.setFont(font)
        self.selecciona_peli_label.setObjectName("selecciona_peli_label")
        self.prediccion_label = QtWidgets.QLabel(self.centralwidget)
        self.prediccion_label.setGeometry(QtCore.QRect(40, 530, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.prediccion_label.setFont(font)
        self.prediccion_label.setObjectName("prediccion_label")
        self.umbral_similitud_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.umbral_similitud_textEdit.setGeometry(QtCore.QRect(390, 90, 61, 31))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.umbral_similitud_textEdit.setFont(font)
        self.umbral_similitud_textEdit.setObjectName("umbral_similitud_textEdit")
        self.umbral_similitud_label = QtWidgets.QLabel(self.centralwidget)
        self.umbral_similitud_label.setGeometry(QtCore.QRect(270, 100, 171, 16))


        

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.umbral_similitud_label.setFont(font)
        self.umbral_similitud_label.setObjectName("umbral_similitud_label")
        self.Items_ranking_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Items_ranking_textEdit.setGeometry(QtCore.QRect(130, 90, 61, 31))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.Items_ranking_textEdit.setFont(font)
        self.Items_ranking_textEdit.setObjectName("Items_ranking_textEdit")
        self.comboBox_Usuario1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Usuario1.setGeometry(QtCore.QRect(200, 60, 69, 22))
        self.comboBox_Usuario1.setObjectName("comboBox_Usuario1")
        self.comboBox_Usuario1.addItems(Usuarios)
        self.comboBox_Usuario2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Usuario2.setGeometry(QtCore.QRect(180, 440, 69, 22))
        self.comboBox_Usuario2.setObjectName("comboBox_Usuario2")
        self.comboBox_Usuario2.addItem('Null')
        self.comboBox_Usuario2.addItems(Usuarios)
        self.ranking_label = QtWidgets.QLabel(self.centralwidget)
        self.ranking_label.setGeometry(QtCore.QRect(380, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.ranking_label.setFont(font)
        self.ranking_label.setObjectName("ranking_label")
        self.resultado_prediccion = QtWidgets.QLabel(self.centralwidget)
        self.resultado_prediccion.setGeometry(QtCore.QRect(120, 530, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.resultado_prediccion.setFont(font)
        self.resultado_prediccion.setText("")
        self.resultado_prediccion.setObjectName("resultado_prediccion")
        self.comboBox_Pelicula = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Pelicula.setGeometry(QtCore.QRect(180, 490, 69, 22))
        self.comboBox_Pelicula.setObjectName("comboBox_Pelicula")
        #self.comboBox_Pelicula.setEnabled(False)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 170, 211, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #AÑADIMOS LAS PELIS NO VISTAS AL COMBO BOX

        self.comboBox_Usuario2.currentTextChanged.connect(self.on_combobox_changed)
        self.Predecir_Button.clicked.connect(self.prueba)
        self.Recomendar_Button.clicked.connect(self.recomendar)   



    def on_combobox_changed(self, value):
        print("combobox changed", value)
        self.cursor.execute('SELECT movieId FROM ratings WHERE userId != ?', (value,))
        result = self.cursor.fetchall()
        pelisNoVistas = []
        for [x] in result:
            var = str(x)
            pelisNoVistas.append(var)
        #print(pelisNoVistas)
        self.comboBox_Pelicula.clear()
        self.comboBox_Pelicula.addItems(pelisNoVistas)

    def prueba(self):
        print("prueba")
        usuario = str(self.comboBox_Usuario2.currentText())
        pelicula =str(self.comboBox_Pelicula.currentText())
        print(usuario, pelicula)
        self.predecir(usuario, pelicula)


    


    def predecir(self, usuario, pelicula):
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
        print( pelisVistas)
        vectoresUsuarioRating = []
        userid_rating = []
        vectoresUsuarioRating = []
        for i in pelisVistas:
            pelicula = i
            userid_rating = []
            vectoresUsuarioRating.append(pelicula) #ID DE LA PELICULA
            #Sacamos todos los usuarios que han dado rating a cada pelio
            #que ha visto el usuario
            self.cursor.execute('SELECT userId, rating FROM ratings WHERE movieId = ?', (pelicula,))
            resultado = self.cursor.fetchall()
            for row in resultado:
                userid_rating.append(row[0]) #Insertamos userId
                userid_rating.append(row[1]) #Rating que le ha dado el usuario
            #userid_rating son todos los userId y ratings de cada pelicula 
            #Añdimos esta lista a la lista global de vectores de usuarios
            #El formato de esta lista es el siguiente movieId, [userId, rating], movieId.....
            vectoresUsuarioRating.append(userid_rating)
        print(vectoresUsuarioRating)
        x = 0
        z = 0
        iguales = []
        movies = []
        rating = []
        for i in vectoresUsuarioRating: #peli [usuario, rating.....], peli......
            vectores =[]
            if x == 0 or x%2==0: #Si es par es el movieId y no lo queremos
                x+=1
                continue
            else: #Si es impar pasamos al vector con los usuarios y ratings
                vectortemporal = i #Vector al completo -> [2, 4.0]
                #print(vectortemporal) 
                for y in vectortemporal:
                    if z == 0 or z%2 ==0:
                        vectores.append(y) #Guardo los userid en una lista para comparar -> [2,5,6,18]
                        
                        #TENEMOS QUE COMPARAR ESTE VECTOR CON EL VECTOR ORIGINAL
                        z+=1
                    else: 
                        rating.append(y) #ratinng de la pelicula
                        z+=1
                        continue
                #print(vectores)
                check = all(item in vectores for item in usuarios)
                if check:
                    iguales.append(vectores)
                    movies.append(x-1) #id de la pelicula
                else:
                    print('Error no son iguales el vector con el vector original')
                x+=1
        if len(iguales) == 0:
            self.resultado_prediccion.setText('Error :(')
            print('No se ha encontrado ningun vector que coincida con el vector original')
        else:
            print(iguales)
       
        return iguales

    def conexionRecomendar(self):
        print("Recomendar")
        ranking = self.Items_ranking_textEdit.toPlainText()
        usuario = str(self.comboBox_Usuario1.currentText())
        umbral = self.umbral_similitud_textEdit.toPlainText()
        print(usuario, ranking, umbral)
        self.recomendar(usuario, ranking, umbral)

    def recomendar(self):
        ranking = self.Items_ranking_textEdit.toPlainText()
        usuario = str(self.comboBox_Usuario1.currentText())
        umbral = self.umbral_similitud_textEdit.toPlainText()
        print('llego')
        print(usuario, ranking, umbral)
        self.cursor.execute('SELECT movieId FROM ratings WHERE userid != ?', (usuario,))
        resultado = self.cursor.fetchall()
        idpelicula = []
        for row in resultado:
            idpelicula.append(row[0])
        # #print(idpelicula)
        x = 0
        print(len(ranking))
        while x <= len(ranking):
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            x+=1
        y = 0
        while y <= len(ranking): #Rows x en 2
            print(idpelicula[y])
            #self.tableWidget.setItem(y, 0, QtGui.QTableWidgetItem(idpelicula[y]))
            y=y+1


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Recomendar_Button.setText(_translate("MainWindow", "Recomendar!"))
        self.Predecir_Button.setText(_translate("MainWindow", "Predecir!"))
        self.recomendaciones_label.setText(_translate("MainWindow", "Recomendaciones"))
        self.items_ranking_label.setText(_translate("MainWindow", "Items ranking"))
        self.selecciona_usuario_label.setText(_translate("MainWindow", "Selecciona un Usuario (ID)"))
        self.selecciona_usuario_label_2.setText(_translate("MainWindow", "Selecciona un Usuario:"))
        self.selecciona_peli_label.setText(_translate("MainWindow", "Selecciona una película:"))
        self.prediccion_label.setText(_translate("MainWindow", "Predicción:"))
        self.umbral_similitud_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">0</span></p></body></html>"))
        self.umbral_similitud_label.setText(_translate("MainWindow", "Umbral de similitud:"))
        self.Items_ranking_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>"))
        self.ranking_label.setText(_translate("MainWindow", "Ranking"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID item"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Prediccion"))
    
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



 #con = sqlite3.connect('movies.db')
        #if con == None:
        #    print("Hola")
        #else:
            #print('Funciona')
        #cursor = con.cursor()