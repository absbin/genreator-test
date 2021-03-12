from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__ (self):
        super(MyWindow,self).__init__()

        self.setGeometry(400, 200, 600, 500)
        self.setWindowTitle("Simple_gui")
        self.initUI()

    def initUI(self): 
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label")
        self.label.move(400, 400)

        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText("Clicked me!")
        self.b1.clicked.connect(self.clicked_me)

    def clicked_me(self):
        print("You clicked me")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    my_gui=MyWindow()
    my_gui.show()
    sys.exit(app.exec_())

window()