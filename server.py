#-*- coding:utf-8 -*-

__author__ = "Samuel Burbano Ramos"
__version__ = "1.0"

from PySide import QtGui, QtCore
from serverGr import Ui_Form
import sys, socket, asyncore, threading

clientes = {}
class MainServer(asyncore.dispatcher):
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind((host, port))
		self.listen(10)

	def handle_accept(self):
		newSocket, address = self.accept()
		for cliente in clientes.values():
			cliente.send( "<b>%s:%d se ha conectado.</b>" % (address[0], address[1]) )
		clientes[address] = newSocket
		print "%s:%d se ha conectado." % (address[0], address[1])
		SecondServer(newSocket)

class SecondServer(asyncore.dispatcher_with_send):
	def handle_read(self):
		mensaje = self.recv(1000)
		if mensaje:
			for cliente in clientes.values():
				cliente.send( "<b>%s:%d</b>: %s" % (self.getpeername()[0], self.getpeername()[1], mensaje) )
		else:
			self.close()

	def handle_close(self):
		print "%s:%d se ha desconectado." % (self.getpeername()[0], self.getpeername()[1])
		del clientes[self.getpeername()]
		for cliente in clientes.values():
			cliente.send( "<b>%s:%d se ha desconectado.</b>" % (self.getpeername()[0], self.getpeername()[1]) )

def crear_server(host, port):
	MainServer(host, port)
	asyncore.loop()

class Window(QtGui.QWidget, Ui_Form):
	def __init__(self):
		super(Window, self).__init__()
		self.setupUi(self)

		self.serverOn.clicked.connect(self.serverData)
		self.serverOff.clicked.connect(self.serverDown)

	def serverData(self):
		host = self.hostTXT.text()
		port = int(self.portTXT.text())
		self.servidor = threading.Thread(target=crear_server, args=(host, port))
		self.servidor.start()
		self.serverOn.setEnabled(False)
		self.serverOff.setEnabled(True)
		self.hostTXT.setEnabled(False)
		self.portTXT.setEnabled(False)

	def serverDown(self):
		self.servidor._Thread__stop()
		self.serverOn.setEnabled(True)
		self.serverOff.setEnabled(False)
		self.hostTXT.setEnabled(True)
		self.portTXT.setEnabled(True)

app = QtGui.QApplication(sys.argv)
w = Window()
w.show()
app.exec_()