# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'picsearch.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PIL import Image


class PicLabel(QtWidgets.QLabel):
    name = str()

    def __init__(self):
        super().__init__()

    def setName(self, name: str):
        self.name = name

    def mouseReleaseEvent(self, event):
        img = Image.open(self.name)
        img.show()


class SearchEdit(QtWidgets.QTextEdit):
    _callback = None

    def __init__(self, parent):
        super().__init__(parent)

    def setCallBack(self, fun):
        self._callback = fun

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Return:
            self._callback()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1309, 861)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = SearchEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(43, 26, 821, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(910, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1090, 30, 151, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('选项1')
        self.comboBox.addItem('选项2')
        self.comboBox.addItem('选项3')
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 140, 1191, 621))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        positions = [(i, j) for i in range(2) for j in range(3)]
        self.labels = dict()
        for (i, j) in positions:
            self.labels[(i, j)] = PicLabel()
            self.labels[(i, j)].setPixmap(QtGui.QPixmap(""))
            self.labels[(i, j)].setScaledContents(True)
            self.gridLayout.addWidget(self.labels[(i, j)], i, j)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 90, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1080, 90, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(930, 90, 131, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1309, 26))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menumenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "搜索"))
        self.pushButton_2.setText(_translate("MainWindow", "<< Prev"))
        self.pushButton_3.setText(_translate("MainWindow", "Next >>"))
        self.label.setText(_translate("MainWindow", "第0页 / 共0页"))
        self.menumenu.setTitle(_translate("MainWindow", "menu"))
