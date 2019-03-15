from PyQt5 import QtGui, QtWidgets, QtCore
import numpy as np
import sys
import math
from output import Ui_PlotForm
import math
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg

class ApplicationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_PlotForm()
        self.ui.setupUi(self)
        self.time  = np.arange(0, 10,0.001) #in sec but step in 1 msec
        self.vector= np.matrix ([0,0,1]) #da range sabt

        pixelIntensity = 50 #depend on pixel choosen
        self.T1 = self.createT1(pixelIntensity)
        self.T2 = self.createT2(pixelIntensity)
        self.PD = self.createPD(pixelIntensity)
        
        #self.ui.rotationAngle.textChanged.connect(self.plot)  #any change in lineEdit text
       
        #self.ui.te.textChanged.connect(self.plot)  #any change in lineEdit text
        #self.ui.tr.textChanged.connect(self.plot)  #any change in lineEdit text
       
        self.ui.Plot.clicked.connect(self.plot)
        
    

    

    def plot(self):
<<<<<<< HEAD
        DecayMx = self.ui.decayMx
        #DecayMy = self.ui.decayMy
        RecoveryMz = self.ui.recoveryMz

        DecayMx.clear()
        #DecayMy.clear()
        RecoveryMz.clear()
=======
        
        self.DecayMx = self.ui.decayMx
        self.DecayMy = self.ui.decayMy
        self.RecoveryMz = self.ui.recoveryMz

        self.ui.decayMx.clear()
        self.ui.decayMy.clear()
        self.ui.recoveryMz.clear()
>>>>>>> 0d19d8395b6dad5cf7a9d2996ac6720495b607f8

        theta = ((float) (self.ui.rotationAngle.text())) #5ly balk not global
        vector = self.rotationAroundYaxisMatrix(theta,self.vector)
        RecoveryDecayMatrix = self.recoveryDecayEquation(self.T1,self.T2,self.PD,vector)
<<<<<<< HEAD
   
        DecayMx.plot(self.time,np.array(RecoveryDecayMatrix[0,:]).ravel())
        #DecayMy.plot(self.time,np.array(RecoveryDecayMatrix[1,:]).ravel())
        RecoveryMz.plot(self.time,np.array(RecoveryDecayMatrix[2,:]).ravel())

        #plot.showGrid(x=True, y=True, alpha=1)
    
=======
        self.Tr = ((float) (self.ui.tr.text())) 
        self.Te = ((float) (self.ui.te.text())) 
>>>>>>> 0d19d8395b6dad5cf7a9d2996ac6720495b607f8
       
        self.DecayMx.plot(self.time,np.array(RecoveryDecayMatrix[0,:]).ravel())
        self.DecayMy.plot(self.time,np.array(RecoveryDecayMatrix[1,:]).ravel())
        self.RecoveryMz.plot(self.time,np.array(RecoveryDecayMatrix[2,:]).ravel())
        self.RecoveryMz.addLine(x=self.Tr)
        self.RecoveryMz.addLine(x=self.Te)
        self.DecayMx.addLine(x=self.Tr)
        self.DecayMx.addLine(x=self.Te)
        
        
        
    def createPD(self,intensity):
        return (1/255)*intensity 
    
    def returnIntensity(self,Pd): # proton intensity vales from 0 till 1 
        return 255*Pd
    
    def createT1 (self,intensity):
        return ((6*intensity)+500)/1000

    def createT2(self,intensity):
        return ((2*intensity)+20)/1000
    
    def mappingT1 (self,T1): #T1 in msec assumption
        return (T1-500)/6

    def mappingT2 (self,T2):  #T1 in msec assumption
        return (T2-20)/2

    def rotationAroundZaxisMatrix(self,theta,vector):
        vector = vector.transpose()
        theta = (math.pi / 180) * theta
        R = np.matrix ([[np.cos(theta),-np.sin(theta),0], [np.sin(theta), np.cos(theta),0]],[0, 0, 1] )
        R = np.dot(R, vector)
        R = R.transpose()
        return np.matrix(R)

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





app = QtWidgets.QApplication(sys.argv)
application = ApplicationWindow()
application.show()
app.exec_()


