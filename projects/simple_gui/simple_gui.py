from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked_me():
    print("You clicked me")
def window():

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400, 200, 600, 500)
    win.setWindowTitle("Simple_gui")

    label = QtWidgets.QLabel(win)
    label.setText("My first label")
    label.move(400, 400)

    b1=QtWidgets.QPushButton(win)
    b1.setText("Clicked me!")
    b1.clicked.connect(clicked_me)

    win.show()
    sys.exit(app.exec_())




for items in sys.argv:
    print("sys.argv : ", items)

window()
