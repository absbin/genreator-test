from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400, 200, 200, 100)
    win.setWindowTitle("Simple_gui")

    label = QtWidgets.QLabel(win)
    label.setText("My first label")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec_())


for items in sys.argv:
    print("sys.argv : ", items)

window()
