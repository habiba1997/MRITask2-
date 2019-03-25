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
from PIL import Image, ImageEnhance
from imageio import imsave, imread
import scipy.io as sio
import io
from time import sleep

        

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
        self.text = '512'
        self.text2 = 'Proton Density'
        self.T1 = np.zeros((512,512))
        self.T2 = np.zeros((512,512))
        self.error_dialog = None
        self.brit = 0
        self.left = False
        self.right = False
        self.coord = []


    def getText2(self, index):
        self.text2 = self.ui.ImageChange.itemText(index)
        self.changePic()

    def getText(self, index):
        self.text = self.ui.comboBox.itemText(index)
        self.changePic()
 
        

    def changePic(self):
        print(self.text, self.text2)
        if self.text == '512' and self.text2 == 'Proton Density':
            self.pixmap = QtGui.QPixmap(self.fileName0)
        if self.text == '120' and self.text2 == 'Proton Density':
            self.pixmap = QtGui.QPixmap(self.fileName0)
            self.pixmap = self.pixmap.scaled(120,120)
        if self.text == '512' and self.text2 == 'T1':
            self.pixmap = QtGui.QPixmap(self.fileName2)
        if self.text == '120' and self.text2 == 'T1':
            self.pixmap = QtGui.QPixmap(self.fileName2)
            self.pixmap = self.pixmap.scaled(120,120)
        if self.text == '512' and self.text2 == 'T2':
            self.pixmap = QtGui.QPixmap(self.fileName3)
        if self.text == '120' and self.text2 == 'T2':
            self.pixmap = QtGui.QPixmap(self.fileName3)
            self.pixmap = self.pixmap.scaled(120,120)
        self.ui.image.point = []


        

    def clearGraphicView(self):
        self.ui.decayMx.clear()
        self.ui.recoveryMz.clear()

    def showError(self):
        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.showMessage("Please select a proper phantom")


    def setImage(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp *.mat)") # Ask for file
        if self.fileName: # If the user gives a file
            if self.fileName.split(".")[1] != "mat":
               return self.showError()
            print(self.fileName)
            output = sio.loadmat (self.fileName)
            img = output['Phantom']
            imgT1 = output['T1']
            imgT2 = output['T2']
            imgT1 = imgT1.astype(np.uint8)
            imgT2 = imgT2.astype(np.uint8)
            img = img.astype(np.uint8)
            imsave("E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\phantom1.png", img)
            imsave("E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\T1.png", imgT1)
            imsave("E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\T2.png", imgT2)
            self.fileName0 = 'E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\phantom1.png'
            self.fileName2 = "E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\T1.png"
            self.fileName3 = "E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\T2.png"
            self.img = cv2.imread(self.fileName0, 0)
            print(self.img.shape)
            self.ui.image.setMouseTracking(False)
            self.ui.image.mousePressEvent = self.getPixel
            self.ui.image.mouseMoveEvent = self.changeCont
            self.ui.rotationAngle.textChanged.connect((self.angleChan))
            self.paint = True
            self.ui.comboBox.activated.connect(self.getText)
            self.ui.ImageChange.activated.connect(self.getText2)
            self.pixmap = QtGui.QPixmap(self.fileName0)
            self.ui.image.setPixmap(self.pixmap)
            print(self.img[self.x,self.y])


    def angleChan(self):
        self.clearGraphicView()
        self.plot()


    def changeCont(self, event):
        if self.ui.checkBox.isChecked():
            if self.left:
                image1 = Image.open(self.fileName0)
                enhancer = ImageEnhance.Brightness(image1)
                self.brit += 0.05
                enhanced_img = enhancer.enhance(self.brit)
                enhanced_img.save('E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\enhanced_img.png')
                self.fileName4 = 'E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\enhanced_img.png'
                self.pixmap5 = QtGui.QPixmap(self.fileName4)
                self.ui.image.setPixmap(self.pixmap5)
                print('sa7')
            if self.right:
                image1 = Image.open(self.fileName0)
                enhancer = ImageEnhance.Brightness(image1)
                self.brit -= 0.05
                enhanced_img = enhancer.enhance(self.brit)
                enhanced_img.save('E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\enhanced_img.png')
                self.fileName4 = 'E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\enhanced_img.png'
                self.pixmap5 = QtGui.QPixmap(self.fileName4)
                self.ui.image.setPixmap(self.pixmap5)
                print('sa7')


    def mousePressEvent(self, e):
        self.points << e.pos()
        self.update()
 
    def passCord(self):
        self.ui.image.point.append([self.x, self.y, self.pen[self.count]])
        self.ui.image.x = self.ui.image.frameGeometry().width()
        self.ui.image.y = self.ui.image.frameGeometry().height()


    def getPixel(self, event):
        if event.button() == Qt.LeftButton:
            self.left = True
            self.right = False
        if event.button() == Qt.RightButton:    #for contrast left and right button
            self.right = True
            self.left = False
        if not self.ui.checkBox.isChecked():
            if self.text == '512':
                self.x = event.pos().x()
                self.y = event.pos().y()
                self.x1 = event.pos().x() * (512 / self.x2)
                self.y1 = event.pos().y() * (512 / self.y2)
                self.x1 = math.floor(self.x1)
                self.y1 = math.floor(self.y1)
                self.T1 = self.createT1(self.img[self.x1,self.y1])
                self.T2 = self.createT2(self.img[self.x1,self.y1])
                self.PD = self.createPD(self.img[self.x1,self.y1])
            if self.text == '120':
                self.x = event.pos().x()
                self.y = event.pos().y()
                self.T1 = self.createT1(self.img[self.x,self.y])
                self.T2 = self.createT2(self.img[self.x,self.y])
                self.PD = self.createPD(self.img[self.x,self.y])
            self.count += 1
            if self.count == 6:
                self.count = -1
            self.pen = [QtGui.QPen(QtCore.Qt.green), QtGui.QPen(QtCore.Qt.red), QtGui.QPen(QtCore.Qt.yellow), QtGui.QPen(QtCore.Qt.blue),
            QtGui.QPen(QtCore.Qt.darkMagenta)]
            self.plot()
            self.passCord()
            self.coord.append([self.x, self.y])


    def optFrame(self):
            if self.ui.image.x != self.ui.image.frameGeometry().width() or self.ui.image.y != self.ui.image.frameGeometry().height():
                self.ui.image.x = self.ui.image.frameGeometry().width()
                self.ui.image.y = self.ui.image.frameGeometry().height()
                k = 0
                for i in self.coord:
                    x = self.coord[k][0]
                    y = self.coord[k][1]
                    print(x, y, self.ui.image.frameGeometry().width(), self.ui.image.frameGeometry().height())
                    self.ui.image.point[k][0] = x / (520 / self.ui.image.frameGeometry().width())
                    self.ui.image.point[k][1] = y / (520 / self.ui.image.frameGeometry().height())
                    k += 1


    def paintEvent(self, event):
        if self.paint and self.count == -1 and not self.ui.checkBox.isChecked():
            self.x2 = self.ui.image.frameGeometry().width()
            self.y2 = self.ui.image.frameGeometry().height()
            self.pixmap0 = self.pixmap
            #pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap0) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()

        if self.paint and self.count == 0 and not self.ui.checkBox.isChecked():    
            #pixmap = QtGui.QPixmap(self.fileName) # Setup pixmap with the provided image
            self.x2 = self.ui.image.frameGeometry().width()
            self.y2 = self.ui.image.frameGeometry().height()
            self.optFrame()
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.clearGraphicView()
            self.ui.image.paint = True
            self.pixmap1 = self.pixmap0
            #pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap0) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            self.paint1 = True
            if self.right:
                self.count = -1
                self.ui.image.point = []
                if self.text == '120':
                    self.pixmap = QtGui.QPixmap(self.fileName0)
                    self.pixmap = self.pixmap.scaled(120,120)
                if self.text == '512':
                    self.pixmap = QtGui.QPixmap(self.fileName0)
                #self.pixmap = self.pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
                self.ui.image.setPixmap(self.pixmap) # Set the pixmap onto the label
                #self.ui.image.adjustSize()
                self.ui.image.setScaledContents(True)
                self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.image.show()
                self.clearGraphicView()
            #self.paint = False  
        if  self.paint1 and self.count == 1 and not self.ui.checkBox.isChecked():
            self.x2 = self.ui.image.frameGeometry().width()
            self.y2 = self.ui.image.frameGeometry().height()
            self.optFrame()
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.clearGraphicView()
            #self.passCord()
            self.pixmap2 = self.pixmap1
            #self.pixmap1 = self.pixmap1.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap1) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            self.paint2 = True
            if self.right:
                self.count = -1
                self.ui.image.point = []
                if self.text == '120':
                    self.pixmap = QtGui.QPixmap(self.fileName0)
                    self.pixmap = self.pixmap.scaled(120,120)
                if self.text == '512':
                    self.pixmap = QtGui.QPixmap(self.fileName0)
                #self.pixmap = self.pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
                self.ui.image.setPixmap(self.pixmap) # Set the pixmap onto the label
                #self.ui.image.adjustSize()
                self.ui.image.setScaledContents(True)
                self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.image.show()
                self.clearGraphicView()
            #self.paint1 = False
        if self.paint2 and self.count == 2 and not self.ui.checkBox.isChecked():
            self.x2 = self.ui.image.frameGeometry().width()
            self.y2 = self.ui.image.frameGeometry().height()
            self.optFrame()
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.clearGraphicView()
            #self.passCord()
            self.pixmap3 = self.pixmap2
            #self.pixmap2 = self.pixmap2.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap2) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show() 
            self.paint3 = True
            if self.right:
                self.count = -1
                self.ui.image.point = []
                if self.text == '120':
                    self.pixmap = QtGui.QPixmap(self.fileName0)
                    self.pixmap = self.pixmap.scaled(120,120)
                if self.text == '512':
                    self.pixmap = QtGui.QPixmap(self.fileName0)
                #self.pixmap = self.pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
                self.ui.image.setPixmap(self.pixmap) # Set the pixmap onto the label
                #self.ui.image.adjustSize()
                self.ui.image.setScaledContents(True)
                self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.image.show()
                self.clearGraphicView()
            #self.paint2 = False
        if self.paint3 and self.count == 3 and not self.ui.checkBox.isChecked():
            self.x2 = self.ui.image.frameGeometry().width()
            self.y2 = self.ui.image.frameGeometry().height()
            self.optFrame()
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.clearGraphicView()
            #self.passCord()
            self.pixmap4 = self.pixmap3
            #self.pixmap3 = self.pixmap3.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap3) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()    
            self.paint4 = True
            if self.right:
                self.count = -1
                self.ui.image.point = []
                if self.text == '120':
                    self.pixmap = QtGui.QPixmap(self.fileName0)
                    self.pixmap = self.pixmap.scaled(120,120)
                if self.text == '512':
                    self.pixmap = QtGui.QPixmap(self.fileName0)
                #self.pixmap = self.pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
                self.ui.image.setPixmap(self.pixmap) # Set the pixmap onto the label
                #self.ui.image.adjustSize()
                self.ui.image.setScaledContents(True)
                self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.image.show()
                self.clearGraphicView()
            #self.paint3 = False     
        if self.paint4 and self.count == 4 and not self.ui.checkBox.isChecked():
            self.x2 = self.ui.image.frameGeometry().width()
            self.y2 = self.ui.image.frameGeometry().height()
            self.optFrame()
            if self.pixmap0 != self.pixmap:
                self.count = -1
                self.clearGraphicView()
            #self.passCord()
            #self.pixmap4 = self.pixmap4.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(self.pixmap4) # Set the pixmap onto the label
            #self.ui.image.adjustSize()
            self.ui.image.setScaledContents(True)
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.show()
            if self.right:
                self.count = -1
                self.ui.image.point = []
                if self.text == '120':
                    self.pixmap = QtGui.QPixmap(self.fileName0)
                    self.pixmap = self.pixmap.scaled(120,120)
                if self.text == '512':
                    self.pixmap = QtGui.QPixmap(self.fileName0)
                #self.pixmap = self.pixmap.scaled(self.ui.image.width(), self.ui.image.height(), QtCore.Qt.KeepAspectRatio)
                self.ui.image.setPixmap(self.pixmap) # Set the pixmap onto the label
                #self.ui.image.adjustSize()
                self.ui.image.setScaledContents(True)
                self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.image.show()
                self.clearGraphicView()
            #self.paint4 = False



    def plot(self):
        
        self.DecayMx = self.ui.decayMx
        self.RecoveryMz = self.ui.recoveryMz
        

        self.theta = ((float) (self.ui.rotationAngle.text())) #5ly balk not global 
        self.Tr = ((float) (self.ui.tr.text()))
        self.Te = ((float) (self.ui.te.text()))
        

        self.Mx = []
        self.Mz =[]
        self.vector= np.matrix ([0,0,1]) #da range sabt
        
        self.vector = self.rotationAroundYaxisMatrix(self.theta,self.vector)

        for i in range(len(self.time)):
            #self.vector = self.rotationAroundZaxisMatrixXY(self.Tr,speed,self.vector,self.time[i])
            self.vector = self.recoveryDecayEquation(self.T1,self.T2,self.PD,self.vector,self.time[i])
            
            self.Mx = np.append(self.Mx,self.vector.item(0))
            self.Mz = np.append(self.Mz,self.vector.item(2))
        
    
        self.DecayMx.plot(self.time,np.ravel(self.Mx))
        self.RecoveryMz.plot(self.time,np.ravel(self.Mz))

        self.RecoveryMz.addLine(x=self.Tr)
        self.RecoveryMz.addLine(x=self.Te)
        self.DecayMx.addLine(x=self.Tr)
        self.DecayMx.addLine(x=self.Te)


    
    def createPD(self,intensity):
        return (1/255)*intensity 

    def createT1(self,intensity):

      
            T1 = (7.5*intensity) + 50

            return T1

    def returnIntensityfromProtonDensity(self,Pd): # proton intensity vales from 0 till 1 
        return 255*Pd
    
    


    
    # a function that returns T2 ( decay time ) based on the intensity
    def createT2(self,intensity):
            T2 = 0.5*intensity
            return T2

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



app = QtWidgets.QApplication(sys.argv)
window = window()
sys.exit(app.exec_())