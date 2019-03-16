# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.t2Plot = PlotWidget(self.tab)
        self.t2Plot.setObjectName("t2Plot")
        self.gridLayout_2.addWidget(self.t2Plot, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 10, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 11, 0, 1, 1)
        self.image = QtWidgets.QLabel(self.tab)
        self.image.setMaximumSize(QtCore.QSize(520, 520))
        self.image.setText("")
        self.image.setObjectName("image")
        self.gridLayout_2.addWidget(self.image, 1, 0, 6, 1)
        self.t1Plot = PlotWidget(self.tab)
        self.t1Plot.setObjectName("t1Plot")
        self.gridLayout_2.addWidget(self.t1Plot, 6, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 1, 1, 1)
        self.browse = QtWidgets.QPushButton(self.tab)
        self.browse.setMaximumSize(QtCore.QSize(120, 16777215))
        self.browse.setObjectName("browse")
        self.gridLayout_2.addWidget(self.browse, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Flip Angel"))
        self.lineEdit.setText(_translate("MainWindow", "90"))
        self.comboBox.setItemText(0, _translate("MainWindow", "520"))
        self.comboBox.setItemText(1, _translate("MainWindow", "180"))
        self.label_2.setText(_translate("MainWindow", "T2"))
        self.label.setText(_translate("MainWindow", "T1"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Phantom Features"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

