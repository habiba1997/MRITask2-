from PyQt5 import QtGui, QtWidgets, QtCore
import numpy as np
import sys
import math
from output import Ui_PlotForm
import math
import numpy as np
import matplotlib.pyplot as plt


class ApplicationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_PlotForm()
        self.ui.setupUi(self)
        self.time  = np.arange(0, 10,0.001) #in sec but step in 1 msec
        self.vector= np.matrix ([0,0,1]) #da range sabt

        pixelIntensity = 200 #depend on pixel choosen
        self.T1 = self.createT1(pixelIntensity)
        self.T2 = self.createT2(pixelIntensity)
        self.PD = self.createPD(pixelIntensity)
        self.ui.rotationAngle.textChanged.connect(self.plot)  #any change in lineEdit text
        self.ui.Plot.clicked.connect(self.plot)

    def plot(self):
        DecayMx = self.ui.decayMx
        DecayMy = self.ui.decayMy
        RecoveryMz = self.ui.recoveryMz

        DecayMx.clear()
        DecayMy.clear()
        RecoveryMz.clear()

        theta = ((float) (self.ui.rotationAngle.text())) #5ly balk not global
        vector = self.rotationAroundYaxisMatrix(theta,self.vector)
        RecoveryDecayMatrix = self.recoveryDecayEquation(self.T1,self.T2,self.PD,vector)
   
        DecayMx.plot(self.time,np.array(RecoveryDecayMatrix[0,:]).ravel())
        DecayMy.plot(self.time,np.array(RecoveryDecayMatrix[1,:]).ravel())
        RecoveryMz.plot(self.time,np.array(RecoveryDecayMatrix[2,:]).ravel())

        #plot.showGrid(x=True, y=True, alpha=1)
    
       

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





app = QtWidgets.QApplication(sys.argv)
application = ApplicationWindow()
application.show()
app.exec_()


