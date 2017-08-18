from backend import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Main(QMainWindow):
	def __init__(self,parent=None):
		QMainWindow.__init__(self,parent)
		self.button()
		self.window()
		self.screen()
	
	def window(self):
		self.setWindowTitle("Text Editor")
		self.resize(400,600)#---------, |(row,col)
	
	def button(self):
		line1 = ["AC","S1","S2","/"]
		row = 0
		for t in line1:
				t = QPushButton(self, text=t)
				t.resize(100,100)
				t.move(row,100)
				row +=100
				t.clicked.connect(self.num)
		
		line2 = ["7","8","9","*"]
		row = 0
		for t in line2:
				t = QPushButton(self, text=t)
				t.resize(100,100)
				t.move(row,200)
				row +=100
				t.clicked.connect(self.num)
		
		line3 = ["4","5","6","-"]
		row = 0
		for t in line3:
				t = QPushButton(self, text=t)
				t.resize(100,100)
				t.move(row,300)
				row +=100
				t.clicked.connect(self.num)
	
		
		line4 = ["1","2","3","+"]
		row = 0
		for t in line4:
				t = QPushButton(self, text=t)
				t.resize(100,100)
				t.move(row,400)
				row +=100
				t.clicked.connect(self.num)
		
		line5 = ["Clear","0",".","="]
		row = 0
		for t in line5:
				t = QPushButton(self, text=t)
				t.resize(100,100)
				t.move(row,500)
				row +=100
				t.clicked.connect(self.num)
		        

	def screen(self):
		
		showup = QLineEdit(self)
		self.showup = showup
		showup.resize(400,100)
		showup.move(0,0)

	def num(self):
		""" self.sender can get text from the button"""
		sender = self.sender()
		if sender.text() == ["Clear",".","=","+","-","*","AC","S1","S2","/"]:
			self.nonNumber(sender.text())
		self.showup.setText(sender.text())

	#def nonNumber(self, symbol):
		#if symbol is "Clear":
			








	
	
	
def main():
	app = QApplication(sys.argv)
	main_window = Main()
	main_window.show()
	app.exec_()

if __name__ == "__main__":
	main()
		

	



