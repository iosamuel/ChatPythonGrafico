# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created: Fri Aug 24 23:09:02 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 339)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/server.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.textChat = QtGui.QTextBrowser(Form)
        self.textChat.setObjectName("textChat")
        self.gridLayout.addWidget(self.textChat, 0, 0, 1, 2)
        self.mensajeUser = QtGui.QTextEdit(Form)
        self.mensajeUser.setObjectName("mensajeUser")
        self.gridLayout.addWidget(self.mensajeUser, 1, 0, 2, 1)
        self.enviarB = QtGui.QPushButton(Form)
        self.enviarB.setObjectName("enviarB")
        self.gridLayout.addWidget(self.enviarB, 1, 1, 1, 1)
        self.limpiarB = QtGui.QPushButton(Form)
        self.limpiarB.setObjectName("limpiarB")
        self.gridLayout.addWidget(self.limpiarB, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Cliente de CHAT", None, QtGui.QApplication.UnicodeUTF8))
        self.enviarB.setText(QtGui.QApplication.translate("Form", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.limpiarB.setText(QtGui.QApplication.translate("Form", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))

