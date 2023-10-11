import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.Qt import Qt

form_class = uic.loadUiType("myomok01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.flag_wb = True
        self.setupUi(self)
        
        for i in range(10):
            for j in range(10):
                piece = QPushButton("", self)
                piece.setIcon(QIcon("0.png"))
                piece.setIconSize(QtCore.QSize(40, 40))
                piece.setGeometry(i*40, j*40, 40, 40)
                piece.clicked.connect(self.click)
        
        self.show()
        
    def click(self):
        if self.flag_wb :
            self.sender().setIcon(QIcon("1.png"))
        else :
            self.sender().setIcon(QIcon("2.png"))
        self.flag_wb = not self.flag_wb

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()