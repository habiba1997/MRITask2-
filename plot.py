import sys
from random import randint
from PyQt5 import QtGui, QtWidgets, QtCore
from gui import Ui_MainWindow
import numpy as np

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.onClick)
        self.draw = False
        self.ui.pushButton.setCheckable(True)

    def onClick(self):
        if self.ui.pushButton.isChecked():
            self.draw = True
            self.plot()
        else:
            self.draw = False
    
    def plot(self):
        arr1 = []
        #arr2 = []
        plotWindow = self.ui.graphicsView
        plotWindow.clear()
        #plot.showGrid(x=True, y=True, alpha=1)
        arr1 = np.matrix([[  1.00000000e+00][  9.24624761e-02][  8.54930948e-03][  7.90490323e-04][  7.30906926e-05][  6.75814641e-06][  6.24874951e-07][  5.77774852e-08][  5.34224934e-09][  4.93957602e-10]])
        A = np.squeeze(np.asarray(arr1))   
        print(A)         #arr2.append(randint(0, 1000))
        plotWindow.plot(A)
           
        
        #print('arr1[0]', arr1[0])
        #print('arr2[0]', arr2[0])

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()