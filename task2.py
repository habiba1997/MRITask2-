# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Study\Third year\Second Term\MRI\Task2\task2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import math
from output import Ui_PlotForm
import traceback
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets, QtQuick
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtQuick import QQuickPaintedItem
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage, QColor, QBrush, QPainter, QPen
from PyQt5.QtCore import Qt
from task2_gui import Ui_MainWindow


        

class window(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.time  = np.arange(0, 10,0.001) #in sec but step in 1 msec
        self.vector= np.matrix ([0,0,1]) #da range sabt

        self.DecayMx = self.ui.t2Plot
        #DecayMy = self.ui.t1Plot
        self.RecoveryMz = self.ui.t1Plot

        self.ui.browse.clicked.connect(self.setImage)
        self.show()
        self.paint = False
        self.paint1 = False
        self.paint2 = False
        self.paint3 = False
        self.paint4 = False
        self.paint5 = False
        self.points = QtGui.QPolygon()
        self.x = 90
        self.y = 90
        self.count = -1
        self.text = '520'

    def getText(self, index):
        self.text = self.ui.comboBox.itemText(index)
        if self.text == '520':
            self.pixmap = QtGui.QPixmap(self.fileName)
            #self.pixmap = self.pixmap.scaled(180,180)

        if self.text == '180':
            self.pixmap = QtGui.QPixmap(self.fileName)
            self.pixmap = self.pixmap.scaled(180,180)
            print('sa7')


    def setImage(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)") # Ask for file
        if self.fileName: # If the user gives a file
            print(self.fileName)
            self.img = cv2.imread(self.fileName, 0)
            print(self.img.shape)
            self.ui.image.mousePressEvent = self.getPixel
            self.ui.lineEdit.textChanged.connect((self.plot))
            self.paint = True
            self.ui.comboBox.activated.connect(self.getText)
            self.pixmap = QtGui.QPixmap(self.fileName)



            print(self.img[self.x,self.y])

    def mousePressEvent(self, e):
        self.points << e.pos()
        self.update()

    def getPixel(self, event):
            self.T1 = self.createT1(self.img[self.x,self.y])
            self.T2 = self.createT2(self.img[self.x,self.y])
            self.PD = self.createPD(self.img[self.x,self.y])
            self.x = event.pos().x()
            self.y = event.pos().y()
            self.count += 1
            print(self.img[self.x, self.y])
            self.DecayMx = self.ui.t2Plot
            self.RecoveryMz = self.ui.t1Plot



            theta = ((float) (self.ui.lineEdit.text())) #5ly balk not global
            vector = self.rotationAroundYaxisMatrix(theta,self.vector)
            RecoveryDecayMatrix = self.recoveryDecayEquation(self.T1,self.T2,self.PD,vector)
    
            self.DecayMx.plot(self.time,np.array(RecoveryDecayMatrix[0,:]).ravel())
            self.RecoveryMz.plot(self.time,np.array(RecoveryDecayMatrix[2,:]).ravel())

            #print(self.count)
            #print(self.x, self.y)
            print(self.paint,"paint1:", self.paint1,"paint2:", self.paint2,"paint3:", self.paint3,"paint4:", self.paint4)
            print("Left Button Clicked") 
            

    def paintEvent(self, event):
        if self.paint and self.count == -1:
            self.pixmap0 = self.pixmap
            #pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap0) # Set the pixmap onto the label
            self.ui.image.adjustSize()
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()

        if self.paint and self.count == 0:    
            #pixmap = QtGui.QPixmap(self.fileName) # Setup pixmap with the provided image
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.ui.t2Plot.clear()
                self.ui.t1Plot.clear()
            painter = QtGui.QPainter(self.pixmap0)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            pen = QtGui.QPen(QtCore.Qt.red)
            painter.setPen(pen)
            painter.drawEllipse(self.x, self.y, 8, 8)
            painter.end()
            self.pixmap1 = self.pixmap0
            #pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap0) # Set the pixmap onto the label
            self.ui.image.adjustSize()
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            self.paint1 = True

            #self.paint = False  
                
        if  self.paint1 and self.count == 1:
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.ui.t2Plot.clear()
                self.ui.t1Plot.clear()
            painter = QtGui.QPainter(self.pixmap1)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QPen(QtCore.Qt.green))
            painter.drawEllipse(self.x, self.y, 8, 8)
            painter.end()
            self.pixmap2 = self.pixmap1
            #self.pixmap1 = self.pixmap1.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap1) # Set the pixmap onto the label
            self.ui.image.adjustSize()
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            self.paint2 = True
            #self.paint1 = False
        if self.paint2 and self.count == 2:
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.ui.t2Plot.clear()
                self.ui.t1Plot.clear()
            painter = QtGui.QPainter(self.pixmap2)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QPen(QtCore.Qt.blue))
            painter.drawEllipse(self.x, self.y, 8, 8)
            painter.end()
            self.pixmap3 = self.pixmap2
            #self.pixmap2 = self.pixmap2.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap2) # Set the pixmap onto the label
            self.ui.image.adjustSize()
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show() 
            self.paint3 = True
            #self.paint2 = False
        if self.paint3 and self.count == 3:
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.ui.t2Plot.clear()
                self.ui.t1Plot.clear()
            painter = QtGui.QPainter(self.pixmap3)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QPen(QtCore.Qt.yellow))
            painter.drawEllipse(self.x, self.y, 8, 8)
            painter.end()
            self.pixmap4 = self.pixmap3
            #self.pixmap3 = self.pixmap3.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap3) # Set the pixmap onto the label
            self.ui.image.adjustSize()
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()    
            self.paint4 = True
            #self.paint3 = False     
        if self.paint4 and self.count == 4:
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.ui.t2Plot.clear()
                self.ui.t1Plot.clear()
            painter = QtGui.QPainter(self.pixmap4)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QPen(QtCore.Qt.darkGray))
            painter.drawEllipse(self.x, self.y, 8, 8)
            painter.end()
            #self.pixmap4 = self.pixmap4.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap4) # Set the pixmap onto the label
            self.ui.image.adjustSize()
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            #self.paint4 = False
        if self.count == 5:
            if self.text == '180':
                self.pixmap = QtGui.QPixmap(self.fileName)
                self.pixmap = self.pixmap.scaled(180,180)
            if self.text == '520':
                self.pixmap = QtGui.QPixmap(self.fileName)
            #self.pixmap = self.pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap0) # Set the pixmap onto the label
            self.ui.image.adjustSize()
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            self.count = -1
            self.paint = True
            self.ui.t2Plot.clear()
            self.ui.t1Plot.clear()


    def plot(self, event):
        self.DecayMx = self.ui.t2Plot
        self.RecoveryMz = self.ui.t1Plot


        theta = ((float) (self.ui.lineEdit.text())) #5ly balk not global
        vector = self.rotationAroundYaxisMatrix(theta,self.vector)
        RecoveryDecayMatrix = self.recoveryDecayEquation(self.T1,self.T2,self.PD,vector)
   
        self.ui.t2Plot.clear()
        self.ui.t1Plot.clear()

        self.DecayMx.plot(self.time,np.array(RecoveryDecayMatrix[0,:]).ravel())
        #DecayMy.plot(self.time,np.array(RecoveryDecayMatrix[1,:]).ravel())
        self.RecoveryMz.plot(self.time,np.array(RecoveryDecayMatrix[2,:]).ravel())

    def createPD(self,intensity):
        return (1/255)*intensity 

    def createT1 (self,intensity):
        return ((6*intensity)+500)/1000

    def createT2(self,intensity):
        return ((2*intensity)+20)/1000


    def rotationAroundYaxisMatrix(self,theta,vector):
        vector = vector.transpose()
        theta = (math.pi / 180) * theta
        R = np.matrix ([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]] )
        R = np.dot(R, vector)
        R = R.transpose()
        return np.matrix(R)

    def recoveryDecayEquation(self,T1,T2,PD,vector):
        vector = vector.transpose()
        Decay =  []
        Rec = []
        for i in range(len(self.time)):
            Decay = np.append(Decay,np.dot([[np.exp(-self.time[i]/T2),0,0],[0,np.exp(-self.time[i]/T2),0],[0,0,np.exp(-self.time[i]/T1)]],vector))
            Rec =  np.append(Rec, np.dot([[0,0,(1-(np.exp(-self.time[i]/T1)))]],PD) )
        
        Decay = np.matrix(Decay)
        Rec =  np.matrix(Rec)
        RD  = Decay + Rec
        RD = RD.reshape(len(self.time),3)
        RD = RD.transpose()
        return RD  




 
        
    
    def Error_mess(self):
        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.showMessage('Oh no!')
        self.label.setPixmap(QtGui.QPixmap(None))
        self.label_2.setPixmap(QtGui.QPixmap(None))      



app = QtWidgets.QApplication(sys.argv)
window = window()
sys.exit(app.exec_())