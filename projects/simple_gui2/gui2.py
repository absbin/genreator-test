# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not NEW this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(323, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.Button1.setAutoFillBackground(False)
        self.Button1.setObjectName("Button1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 50, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 323, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW = QtWidgets.QAction(MainWindow)
        self.actionNEW.setObjectName("actionNEW")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPast = QtWidgets.QAction(MainWindow)
        self.actionPast.setObjectName("actionPast")
        self.menufile.addAction(self.actionNEW)
        self.menufile.addAction(self.actionOpen)
        self.menuedit.addAction(self.actionCopy)
        self.menuedit.addAction(self.actionPast)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionNEW.triggered.connect(lambda: self.clicked("New was clicked"))
        self.actionOpen.triggered.connect(lambda: self.clicked("Open was clicked"))
        self.actionCopy.triggered.connect(lambda: self.clicked("Copy was clicked"))
        self.actionPast.triggered.connect(lambda: self.clicked("Paste was clicked"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.actionNEW.setText(_translate("MainWindow", "NEW"))
        self.actionNEW.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNEW.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open  a file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy a file"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPast.setText(_translate("MainWindow", "Past"))
        self.actionPast.setStatusTip(_translate("MainWindow", "Paset something"))
        self.actionPast.setShortcut(_translate("MainWindow", "Ctrl+V"))
    def clicked(self,text):
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
