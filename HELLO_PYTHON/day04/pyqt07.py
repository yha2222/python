from PyQt5 import QtWidgets, uic
import sys
from random import random

form_window = uic.loadUiType("pyqt07.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        me = self.le_mine.text()
        com = ''
        result = ''
        
        rnd = random()
        if rnd > 0.66 :
            com = '가위'
        elif rnd > 0.33 :
            com = '바위'
        else :
            com = '보'
            
        if com == "가위" and me == "가위": result = "비김"
        if com == "가위" and me == "바위": result = "이김"
        if com == "가위" and me == "보": result = "짐"
        
        if com == "바위" and me == "가위": result = "짐"
        if com == "바위" and me == "바위": result = "비김"
        if com == "바위" and me == "보": result = "이김"
        
        if com == "보" and me == "가위": result = "이김"
        if com == "보" and me == "바위": result = "짐"
        if com == "보" and me == "보": result = "비김"
        
        self.le_com.setText(com)
        self.le_result.setText(result)

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    main_Window = UiMainWindow() 
    sys.exit(app.exec_())