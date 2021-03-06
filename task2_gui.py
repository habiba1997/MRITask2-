# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task22.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1602, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.image = Label(self.centralwidget)
        #self.image.setMinimumSize(QtCore.QSize(512, 512))
        self.image.setMaximumSize(QtCore.QSize(512, 512))
        self.image.setText("")
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 0, 1, 1)
        self.ImageChange = QtWidgets.QComboBox(self.centralwidget)
        self.ImageChange.setMaximumSize(QtCore.QSize(120, 16777215))
        self.ImageChange.setObjectName("ImageChange")
        self.ImageChange.addItem("")
        self.ImageChange.addItem("")
        self.ImageChange.addItem("")
        self.gridLayout.addWidget(self.ImageChange, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 1)
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setMaximumSize(QtCore.QSize(120, 16777215))
        self.browse.setObjectName("browse")
        self.gridLayout.addWidget(self.browse, 5, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tr = QtWidgets.QLineEdit(self.tab)
        self.tr.setObjectName("tr")
        self.gridLayout_2.addWidget(self.tr, 17, 3, 1, 1)
        self.rotationAngle = QtWidgets.QLineEdit(self.tab)
        self.rotationAngle.setMaximumSize(QtCore.QSize(400, 16777215))
        self.rotationAngle.setObjectName("rotationAngle")
        self.gridLayout_2.addWidget(self.rotationAngle, 17, 0, 1, 1)
        self.te = QtWidgets.QLineEdit(self.tab)
        self.te.setObjectName("te")
        self.gridLayout_2.addWidget(self.te, 17, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 16, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 16, 1, 1, 1)
        self.recoveryMz = PlotWidget(self.tab)
        self.recoveryMz.setMaximumSize(QtCore.QSize(600, 16777215))
        self.recoveryMz.setObjectName("recoveryMz")
        self.gridLayout_2.addWidget(self.recoveryMz, 11, 1, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 16, 3, 1, 1)
        self.decayMx = PlotWidget(self.tab)
        self.decayMx.setMaximumSize(QtCore.QSize(600, 600))
        self.decayMx.setObjectName("decayMx")
        self.gridLayout_2.addWidget(self.decayMx, 1, 1, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 10, 1, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.mriSequence = QtWidgets.QWidget()
        self.mriSequence.setObjectName("mriSequence")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.mriSequence)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TR = QtWidgets.QLineEdit(self.mriSequence)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TR.setFont(font)
        self.TR.setObjectName("TR")
        self.gridLayout_3.addWidget(self.TR, 2, 2, 1, 1)
        self.TE = QtWidgets.QLineEdit(self.mriSequence)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TE.setFont(font)
        self.TE.setObjectName("TE")
        self.gridLayout_3.addWidget(self.TE, 2, 1, 1, 1)
        self.Reconstruction = QtWidgets.QPushButton(self.mriSequence)
        self.Reconstruction.setObjectName("Reconstruction")
        self.gridLayout_3.addWidget(self.Reconstruction, 3, 1, 1, 1)
        self.flipAngle = QtWidgets.QLineEdit(self.mriSequence)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.flipAngle.setFont(font)
        self.flipAngle.setObjectName("flipAngle")
        self.gridLayout_3.addWidget(self.flipAngle, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.mriSequence)
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gillius ADF No2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.mriSequence)
        self.label_7.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Gillius ADF No2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.mriSequence)
        self.label_8.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gillius ADF No2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Constructed = QtWidgets.QLabel(self.mriSequence)
        self.Constructed.setMinimumSize(QtCore.QSize(512, 512))
        self.Constructed.setMaximumSize(QtCore.QSize(512, 512))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Constructed.setFont(font)
        self.Constructed.setAlignment(QtCore.Qt.AlignCenter)
        self.Constructed.setObjectName("Constructed")
        self.gridLayout_4.addWidget(self.Constructed, 0, 1, 1, 1)
        self.FourierMatrix = QtWidgets.QLabel(self.mriSequence)
        self.FourierMatrix.setMinimumSize(QtCore.QSize(512, 512))
        self.FourierMatrix.setMaximumSize(QtCore.QSize(512, 512))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.FourierMatrix.setFont(font)
        self.FourierMatrix.setAlignment(QtCore.Qt.AlignCenter)
        self.FourierMatrix.setObjectName("FourierMatrix")
        self.gridLayout_4.addWidget(self.FourierMatrix, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.mriSequence, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 6, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1602, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ImageChange.setItemText(0, _translate("MainWindow", "Proton Density"))
        self.ImageChange.setItemText(1, _translate("MainWindow", "T1"))
        self.ImageChange.setItemText(2, _translate("MainWindow", "T2"))
        self.comboBox.setCurrentText(_translate("MainWindow", "512"))
        self.comboBox.setItemText(0, _translate("MainWindow", "512"))
        self.comboBox.setItemText(1, _translate("MainWindow", "120"))
        self.checkBox.setText(_translate("MainWindow", "Brightness"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.tr.setText(_translate("MainWindow", "0.8"))
        self.rotationAngle.setText(_translate("MainWindow", "90"))
        self.te.setText(_translate("MainWindow", "0.4"))
        self.label_3.setText(_translate("MainWindow", "Flip Angle"))
        self.label_5.setText(_translate("MainWindow", "Time to Echo"))
        self.label_9.setText(_translate("MainWindow", "Time Repeat"))
        self.label_10.setText(_translate("MainWindow", "Decay In X axis"))
        self.label_12.setText(_translate("MainWindow", "Recovery In Z axis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Phantom Features"))
        self.TR.setText(_translate("MainWindow", "3000"))
        self.TE.setText(_translate("MainWindow", "50"))
        self.Reconstruction.setText(_translate("MainWindow", "Start"))
        self.flipAngle.setText(_translate("MainWindow", "90"))
        self.label_6.setText(_translate("MainWindow", "TE"))
        self.label_7.setText(_translate("MainWindow", "Flip Angle"))
        self.label_8.setText(_translate("MainWindow", "TR"))
        self.Constructed.setText(_translate("MainWindow", "Constructed"))
        self.FourierMatrix.setText(_translate("MainWindow", "FourierMatrix"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mriSequence), _translate("MainWindow", "MRI Sequence"))

from pyqtgraph import PlotWidget

class Label(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(Label, self).__init__(parent=parent)
        self.paint = False
        self.paint1 = False
        self.x = 0
        self.y = 0
        self.count = 0
        self.point = []
        self.pixel = []
    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        for self.pixel in self.point:
                painter.setPen(self.pixel[2])
                painter.drawEllipse(self.pixel[0], self.pixel[1], 8, 8)

