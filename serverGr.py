# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created: Fri Aug 24 19:41:12 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(221, 198)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/server.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.descripcionLabel = QtGui.QLabel(Form)
        self.descripcionLabel.setEnabled(True)
        self.descripcionLabel.setAcceptDrops(False)
        self.descripcionLabel.setAutoFillBackground(False)
        self.descripcionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.descripcionLabel.setObjectName("descripcionLabel")
        self.gridLayout_2.addWidget(self.descripcionLabel, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelHost = QtGui.QLabel(Form)
        self.labelHost.setObjectName("labelHost")
        self.gridLayout.addWidget(self.labelHost, 0, 0, 1, 1)
        self.hostTXT = QtGui.QLineEdit(Form)
        self.hostTXT.setInputMask("")
        self.hostTXT.setObjectName("hostTXT")
        self.gridLayout.addWidget(self.hostTXT, 0, 1, 1, 1)
        self.labelPort = QtGui.QLabel(Form)
        self.labelPort.setObjectName("labelPort")
        self.gridLayout.addWidget(self.labelPort, 1, 0, 1, 1)
        self.portTXT = QtGui.QLineEdit(Form)
        self.portTXT.setObjectName("portTXT")
        self.gridLayout.addWidget(self.portTXT, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.serverOn = QtGui.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/PlayIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.serverOn.setIcon(icon1)
        self.serverOn.setIconSize(QtCore.QSize(20, 20))
        self.serverOn.setCheckable(False)
        self.serverOn.setAutoDefault(False)
        self.serverOn.setDefault(False)
        self.serverOn.setFlat(False)
        self.serverOn.setObjectName("serverOn")
        self.gridLayout_2.addWidget(self.serverOn, 2, 0, 1, 1)
        self.serverOff = QtGui.QPushButton(Form)
        self.serverOff.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/StopIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.serverOff.setIcon(icon2)
        self.serverOff.setIconSize(QtCore.QSize(20, 20))
        self.serverOff.setObjectName("serverOff")
        self.gridLayout_2.addWidget(self.serverOff, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Servidor de CHAT", None, QtGui.QApplication.UnicodeUTF8))
        self.descripcionLabel.setText(QtGui.QApplication.translate("Form", "Servidor de CHAT", None, QtGui.QApplication.UnicodeUTF8))
        self.labelHost.setText(QtGui.QApplication.translate("Form", "Host:", None, QtGui.QApplication.UnicodeUTF8))
        self.hostTXT.setText(QtGui.QApplication.translate("Form", "127.0.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPort.setText(QtGui.QApplication.translate("Form", "Puerto:", None, QtGui.QApplication.UnicodeUTF8))
        self.portTXT.setText(QtGui.QApplication.translate("Form", "9090", None, QtGui.QApplication.UnicodeUTF8))
        self.serverOn.setText(QtGui.QApplication.translate("Form", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.serverOff.setText(QtGui.QApplication.translate("Form", "Apagar", None, QtGui.QApplication.UnicodeUTF8))

