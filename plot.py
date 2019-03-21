import sys
import math
from output import Ui_PlotForm
import traceback
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage, QColor, QBrush, QPainter, QPen, QDragEnterEvent
from PyQt5.QtCore import Qt
from task2_gui import Ui_MainWindow
from PIL import Image
from imageio import imsave, imread
import scipy.io as sio

        

class window(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.time  = np.arange(0,10,0.001) #in sec but step in 1 msec
        self.vector= np.matrix ([0,0,1]) #da range sabt

        #self.DecayMx = self.ui.decayMx
        #self.RecoveryMz = self.ui.recoveryMz
               
        self.DecayMx = self.ui.decayMx
        self.DecayMy = self.ui.decayMy
        self.RecoveryMz = self.ui.recoveryMz

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
        self.text2 = 'Proton Density'
        self.T1 = np.zeros((512,512))
        self.T2 = np.zeros((512,512))

    def getText2(self, index):
        self.text2 = self.ui.ImageChange.itemText(index)
        self.changePic()

    def getText(self, index):
        self.text = self.ui.comboBox.itemText(index)
        self.changePic()

    def changePic(self):
        print(self.text, self.text2)
        if self.text == '520' and self.text2 == 'Proton Density':
            self.pixmap = QtGui.QPixmap(self.fileName0)
        if self.text == '120' and self.text2 == 'Proton Density':
            self.pixmap = QtGui.QPixmap(self.fileName0)
            self.pixmap = self.pixmap.scaled(120,120)
        if self.text == '520' and self.text2 == 'T1':
            self.pixmap = QtGui.QPixmap(self.fileName2)
        if self.text == '120' and self.text2 == 'T1':
            self.pixmap = QtGui.QPixmap(self.fileName2)
            self.pixmap = self.pixmap.scaled(120,120)
        if self.text == '520' and self.text2 == 'T2':
            self.pixmap = QtGui.QPixmap(self.fileName3)
        if self.text == '120' and self.text2 == 'T2':
            self.pixmap = QtGui.QPixmap(self.fileName3)
            self.pixmap = self.pixmap.scaled(120,120)

        

    def clearGraphicView(self):
        self.ui.decayMx.clear()
        self.ui.recoveryMz.clear()
        self.ui.decayMy.clear()

    def setImage(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp *.mat)") # Ask for file
        if self.fileName: # If the user gives a file
            print(self.fileName)
            output = sio.loadmat (self.fileName)
            img = output['iphone']
            img = img.astype(np.uint8)
            imsave("E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\phantom1.png", img)
            self.fileName0 = 'E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\phantom1.png'
            self.img = cv2.imread(self.fileName0, 0)
            self.createT1AndT2ArrayForCombBox()
            print(self.img.shape)
            self.ui.image.mousePressEvent = self.getPixel
            self.ui.rotationAngle.textChanged.connect((self.plot))
            self.paint = True
            self.ui.comboBox.activated.connect(self.getText)
            self.ui.ImageChange.activated.connect(self.getText2)
            self.pixmap = QtGui.QPixmap(self.fileName0)


            print(self.img[self.x,self.y])

    def mousePressEvent(self, e):
        self.points << e.pos()
        self.update()

    def getPixel(self, event):
            self.x2 = self.ui.image.frameGeometry().width()
            self.y2 = self.ui.image.frameGeometry().height()
            if self.text == '520':
                siz = 520
                self.x = event.pos().x() * (siz / self.x2)
                self.y = event.pos().y() * (siz / self.y2)
                self.x = math.floor(self.x)
                self.y = math.floor(self.y)
                self.T1 = self.createT1(self.img[self.x,self.y])
                self.T2 = self.createT2(self.img[self.x,self.y])
                self.PD = self.createPD(self.img[self.x,self.y])
            if self.text == '120':
                siz = 120
                self.x0 = event.pos().x()
                self.y0 = event.pos().y()
                self.x = self.x0 * (siz / self.x2)
                self.y = self.y0 * (siz / self.y2)
                self.x = math.floor(self.x)
                self.y = math.floor(self.y)
                self.T1 = self.createT1(self.img[self.x0,self.y0])
                self.T2 = self.createT2(self.img[self.x0,self.y0])
                self.PD = self.createPD(self.img[self.x0,self.y0])
            
            self.count += 1
            print(self.img[self.x, self.y])
            self.plot()
            #print(self.count)
            #print(self.x, self.y)
            print(self.paint,"paint1:", self.paint1,"paint2:", self.paint2,"paint3:", self.paint3,"paint4:", self.paint4)
            print("Left Button Clicked") 
            

    def paintEvent(self, event):
        if self.paint and self.count == -1:
            self.pixmap0 = self.pixmap
            #pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap0) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()

        if self.paint and self.count == 0:    
            #pixmap = QtGui.QPixmap(self.fileName) # Setup pixmap with the provided image
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.clearGraphicView()
            painter = QtGui.QPainter(self.pixmap0)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            pen = QtGui.QPen(QtCore.Qt.red)
            painter.setPen(pen)
            painter.drawEllipse(self.x, self.y, 8, 8)
            painter.end()
            self.pixmap1 = self.pixmap0
            #pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap0) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            self.paint1 = True

            #self.paint = False  

        if  self.paint1 and self.count == 1:
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.clearGraphicView()
            painter = QtGui.QPainter(self.pixmap1)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QPen(QtCore.Qt.green))
            painter.drawEllipse(self.x, self.y, 8, 8)
            painter.end()
            self.pixmap2 = self.pixmap1
            #self.pixmap1 = self.pixmap1.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap1) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            self.paint2 = True
            #self.paint1 = False
        if self.paint2 and self.count == 2:
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.clearGraphicView()
            painter = QtGui.QPainter(self.pixmap2)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QPen(QtCore.Qt.blue))
            painter.drawEllipse(self.x, self.y, 8, 8)
            painter.end()
            self.pixmap3 = self.pixmap2
            #self.pixmap2 = self.pixmap2.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap2) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show() 
            self.paint3 = True
            #self.paint2 = False
        if self.paint3 and self.count == 3:
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.clearGraphicView()
            painter = QtGui.QPainter(self.pixmap3)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QPen(QtCore.Qt.yellow))
            painter.drawEllipse(self.x, self.y, 8, 8)
            painter.end()
            self.pixmap4 = self.pixmap3
            #self.pixmap3 = self.pixmap3.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap3) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()    
            self.paint4 = True
            #self.paint3 = False     
        if self.paint4 and self.count == 4:
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.clearGraphicView()
            painter = QtGui.QPainter(self.pixmap4)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QPen(QtCore.Qt.darkGray))
            painter.drawEllipse(self.x, self.y, 8, 8)
            painter.end()
            #self.pixmap4 = self.pixmap4.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap4) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            #self.paint4 = False
        if self.count == 5:
            if self.text == '120':
                self.pixmap = QtGui.QPixmap(self.fileName0)
                self.pixmap = self.pixmap.scaled(120,120)
            if self.text == '520':
                self.pixmap = QtGui.QPixmap(self.fileName0)
            #self.pixmap = self.pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            self.count = -1
            self.paint = True
            self.clearGraphicView()


    def plot(self):
        
        self.DecayMx = self.ui.decayMx
        self.DecayMy = self.ui.decayMy
        self.RecoveryMz = self.ui.recoveryMz
        

        self.theta = ((float) (self.ui.rotationAngle.text())) #5ly balk not global 
        self.Tr = ((float) (self.ui.tr.text()))
        self.Te = ((float) (self.ui.te.text()))
        

        self.Mx = []
        self.My = []
        self.Mz =[]
        self.vector= np.matrix ([0,0,1]) #da range sabt
        
        self.vector = self.rotationAroundYaxisMatrix(self.theta,self.vector)

        for i in range(len(self.time)):
            #self.vector = self.rotationAroundZaxisMatrixXY(self.Tr,speed,self.vector,self.time[i])
            self.vector = self.recoveryDecayEquation(self.T1,self.T2,self.PD,self.vector,self.time[i])
            
            self.Mx = np.append(self.Mx,self.vector.item(0))
            self.My = np.append(self.My,self.vector.item(1))
            self.Mz = np.append(self.Mz,self.vector.item(2))
        
    
        self.DecayMx.plot(self.time,np.ravel(self.Mx))
        self.DecayMy.plot(self.time,np.ravel(self.My))
        self.RecoveryMz.plot(self.time,np.ravel(self.Mz))

        self.RecoveryMz.addLine(x=self.Tr)
        self.RecoveryMz.addLine(x=self.Te)
        self.DecayMx.addLine(x=self.Tr)
        self.DecayMx.addLine(x=self.Te)


    
    def createPD(self,intensity):
        return (1/255)*intensity 

    def createT1(self,intensity):

        if intensity == 100: #Gray matter
            T1=900
            
        elif intensity == 255: #white matter
            T1= 510
        
        elif intensity == 200: #muscle
            T1=900
        
        elif intensity == 120 : #fat
            T1=300
            
        elif intensity == 25: #protein
            T1=250
            
        elif intensity == 0: #Black => air
            T1=10
            
        else: # general case for any phantom whatever its intensity 
            T1 = (7.5*intensity) + 50

        return T1

    def returnIntensityfromProtonDensity(self,Pd): # proton intensity vales from 0 till 1 
        return 255*Pd
    
    
    def mappingT1 (self,T1): #T1 in msec assumption
        return (T1-500)/6

    def mappingT2 (self,T2):  #T1 in msec assumption
        return (T2-20)/2

    
    # a function that returns T2 ( decay time ) based on the intensity
    def createT2(self,intensity):

        if intensity == 100: #Gray matter
            T2 =90
    
        elif intensity == 255: #white matter       
            T2 =70

        elif intensity == 200: #muscle        
            T2 = 50

        elif intensity == 120 : #fat        
            T2 = 100

        elif intensity == 25: #protein       
            T2 = 30

        elif intensity == 0: #Black => air        
            T2=1

        else: # general case for any phantom whatever its intensity 
            T2 = 0.5*intensity

        return T2

    def createT1AndT2ArrayForCombBox(self):
        for i in range(self.img.shape[0]):
            for j in range(self.img.shape[1]):
                self.T1[i,j]=self.mappingT1( self.createT1(self.img[i,j]))
                self.T2[i,j]=self.mappingT2( self.createT2(self.img[i,j]))
        self.T1 = self.T1.astype(np.uint8)
        self.T2 = self.T2.astype(np.uint8)
        img2 = Image.fromarray(self.T2)
        img = Image.fromarray(self.T1)
        imsave("E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\T1.png", img)
        imsave("E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\T2.png", img2)
        self.fileName2 = "E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\T1.png"
        self.fileName3 = "E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\T2.png"
        print(self.fileName2)
        print(self.fileName3)

    def rotationAroundYaxisMatrix(self,theta,vector):
            vector = vector.transpose()
            theta = (math.pi / 180) * theta
            R = np.matrix ([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]] )
            R = np.dot(R, vector)
            R = R.transpose()
            return np.matrix(R)


    def rotationAroundZaxisMatrixXY(self,TR,speed,vector,time): #time = self.time
            vector = vector.transpose()
            theta = speed * (time/ TR)
            theta = (math.pi / 180) * theta
            XY = np.matrix([[np.cos(theta),-np.sin(theta),0], [np.sin(theta), np.cos(theta),0],[0, 0, 1]])
            XY = np.dot(XY,vector)
            XY = XY.transpose()
            return np.matrix(XY) 


    def recoveryDecayEquation(self,T1,T2,PD,vector,time):
            vector = vector.transpose()
            Decay =np.matrix([[np.exp(-time/T2),0,0],[0,np.exp(-time/T2),0],[0,0,np.exp(-time/T1)]])
            Decay = np.dot(Decay,vector)
        
            Rec= np.dot(np.matrix([[0,0,(1-(np.exp(-time/T1)))]]),PD)
            Rec = Rec.transpose()
            Decay = np.matrix(Decay)
            Rec =  np.matrix(Rec)    
        
            RD  = Decay + Rec
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