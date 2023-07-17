# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nateh\PycharmProjects\pyChatServer\pyChatGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 849)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.host_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.host_groupBox.setGeometry(QtCore.QRect(10, 10, 481, 182))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.host_groupBox.setFont(font)
        self.host_groupBox.setStyleSheet("")
        self.host_groupBox.setObjectName("host_groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.host_groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 231, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.port_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.port_label.setFont(font)
        self.port_label.setObjectName("port_label")
        self.gridLayout_2.addWidget(self.port_label, 1, 0, 1, 1)
        self.port_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.port_lineEdit.setFont(font)
        self.port_lineEdit.setObjectName("port_lineEdit")
        self.gridLayout_2.addWidget(self.port_lineEdit, 0, 2, 1, 1)
        self.serverIP_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.serverIP_label.setFont(font)
        self.serverIP_label.setObjectName("serverIP_label")
        self.gridLayout_2.addWidget(self.serverIP_label, 0, 0, 1, 1)
        self.serverIP_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.serverIP_lineEdit.setFont(font)
        self.serverIP_lineEdit.setObjectName("serverIP_lineEdit")
        self.gridLayout_2.addWidget(self.serverIP_lineEdit, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 0, 1, 2, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.shutdownServer_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.shutdownServer_pushButton.setFont(font)
        self.shutdownServer_pushButton.setObjectName("shutdownServer_pushButton")
        self.gridLayout_3.addWidget(self.shutdownServer_pushButton, 2, 0, 1, 1)
        self.establishServer_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.establishServer_pushButton.setFont(font)
        self.establishServer_pushButton.setObjectName("establishServer_pushButton")
        self.gridLayout_3.addWidget(self.establishServer_pushButton, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.serverLog_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.serverLog_groupBox.setGeometry(QtCore.QRect(10, 200, 481, 601))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.serverLog_groupBox.setFont(font)
        self.serverLog_groupBox.setObjectName("serverLog_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.serverLog_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.clearLog_pushButton = QtWidgets.QPushButton(self.serverLog_groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.clearLog_pushButton.setFont(font)
        self.clearLog_pushButton.setObjectName("clearLog_pushButton")
        self.gridLayout.addWidget(self.clearLog_pushButton, 1, 0, 1, 1)
        self.serverActivityLog_textEdit = QtWidgets.QTextEdit(self.serverLog_groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.serverActivityLog_textEdit.setFont(font)
        self.serverActivityLog_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.serverActivityLog_textEdit.setObjectName("serverActivityLog_textEdit")
        self.gridLayout.addWidget(self.serverActivityLog_textEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyChat Server"))
        self.host_groupBox.setTitle(_translate("MainWindow", "Host"))
        self.port_label.setText(_translate("MainWindow", "Port"))
        self.serverIP_label.setText(_translate("MainWindow", "ServerIP"))
        self.shutdownServer_pushButton.setText(_translate("MainWindow", "Shutdown Server"))
        self.establishServer_pushButton.setText(_translate("MainWindow", "Establish Server"))
        self.serverLog_groupBox.setTitle(_translate("MainWindow", "Server Activity"))
        self.clearLog_pushButton.setText(_translate("MainWindow", "Clear"))
