#-*- coding:utf-8 -*-

__author__ = "Samuel Burbano Ramos"
__version__ = "1.0"

from PySide import QtGui, QtCore
from clientGr import Ui_Form
from dialog_conf_client import Ui_Dialog
import sys, socket, thread

cliente = socket.socket()
def cliente_con(host, port):
	cliente.connect((host, port))

class Dialogo(QtGui.QDialog, Ui_Dialog):
	def __init__(self):
		super(Dialogo, self).__init__()
		self.setupUi(self)

class ReturnEnterEvent(QtCore.QObject):
	def __init__(self, parent):
		super(ReturnEnterEvent, self).__init__(parent)
		self.parent = parent

	def eventFilter(self, object, event):
		if event.type() == QtCore.QEvent.KeyPress:
			if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
				self.parent.emit(QtCore.SIGNAL("returnPressedOwn()"))
				return True
		return False

class Window(QtGui.QWidget, Ui_Form):
	def __init__(self):
		super(Window, self).__init__()
		d = Dialogo()
		if d.exec_():
			host = d.hostTXT.text()
			port = int(d.portTXT.text())
			cliente_con(host, port)
		else:
			exit()

		self.reciveMensaje()

		self.setupUi(self)

		self.enviarB.clicked.connect(self.enviarMensaje)
		self.limpiarB.clicked.connect(self.limpiar)
		self.connect(self, QtCore.SIGNAL("agregarMensaje(QString)"), self.addMensaje)
		self.connect(self, QtCore.SIGNAL("returnPressedOwn()"), self.enviarMensaje)

		self.filter = ReturnEnterEvent(self)
		self.mensajeUser.installEventFilter(self.filter)

	def limpiar(self):
		self.mensajeUser.clear()
		self.mensajeUser.setFocus()

	def enviarMensaje(self):
		mensaje = self.mensajeUser.toPlainText()
		cliente.send(mensaje)

	def addMensaje(self, mensaje):
		self.textChat.append(mensaje+"\n")
		self.mensajeUser.clear()
		self.mensajeUser.setFocus()

	def reciveMensaje(self):
		def loop():
			while True:
				mensaje = cliente.recv(1000)
				if mensaje:
					self.emit(QtCore.SIGNAL("agregarMensaje(QString)"), mensaje)

		thread.start_new_thread(loop, ())

app = QtGui.QApplication(sys.argv)
w = Window()
w.show()
app.exec_()