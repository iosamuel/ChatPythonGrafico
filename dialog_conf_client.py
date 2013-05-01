# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_conf_client.ui'
#
# Created: Fri Aug 24 23:32:26 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(309, 116)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/server.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.hostLabel = QtGui.QLabel(Dialog)
        self.hostLabel.setObjectName("hostLabel")
        self.gridLayout.addWidget(self.hostLabel, 0, 0, 1, 1)
        self.hostTXT = QtGui.QLineEdit(Dialog)
        self.hostTXT.setObjectName("hostTXT")
        self.gridLayout.addWidget(self.hostTXT, 0, 1, 1, 1)
        self.portLabel = QtGui.QLabel(Dialog)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout.addWidget(self.portLabel, 1, 0, 1, 1)
        self.portTXT = QtGui.QLineEdit(Dialog)
        self.portTXT.setObjectName("portTXT")
        self.gridLayout.addWidget(self.portTXT, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Configuracion de Coneccion", None, QtGui.QApplication.UnicodeUTF8))
        self.hostLabel.setText(QtGui.QApplication.translate("Dialog", "Host:", None, QtGui.QApplication.UnicodeUTF8))
        self.hostTXT.setText(QtGui.QApplication.translate("Dialog", "127.0.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.portLabel.setText(QtGui.QApplication.translate("Dialog", "Puerto:", None, QtGui.QApplication.UnicodeUTF8))
        self.portTXT.setText(QtGui.QApplication.translate("Dialog", "9090", None, QtGui.QApplication.UnicodeUTF8))

