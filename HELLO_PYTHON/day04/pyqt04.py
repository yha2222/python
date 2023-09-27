from PyQt5 import QtWidgets, uic
import sys
from random import random
from PyQt5.Qt import QPlainTextEdit

form_window = uic.loadUiType("pyqt04.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        arr = [
            1, 2, 3, 4, 5,       6, 7, 8, 9, 10,
            11, 12, 13, 14, 15,  16, 17, 18, 19, 20,
            21, 22, 23, 24, 25,  26, 27, 28, 29, 30,
            31, 32, 33, 34, 35,  36, 37, 38, 39, 40,
            41, 42, 43, 44, 45
        ]
        for i in range(1000):
            rnd = int(random() * 45)
            a = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = a
            
       # QPlainTextEdit().setPlainText()
        self.pte01.setPlainText(str(arr[0]));
        self.pte02.setPlainText(str(arr[1]));
        self.pte03.setPlainText(str(arr[2]));
        self.pte04.setPlainText(str(arr[3]));
        self.pte05.setPlainText(str(arr[4]));
        self.pte06.setPlainText(str(arr[5]));
        
if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    main_Window = UiMainWindow() 
    sys.exit(app.exec_())