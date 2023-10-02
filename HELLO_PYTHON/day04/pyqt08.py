from PyQt5 import QtWidgets, uic
import sys
from random import random
from PyQt5.Qt import QPlainTextEdit

form_window = uic.loadUiType("pyqt08.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
    
    def getStar(self, cnt):
        ret = ""
        for i in range(cnt) :
            ret += "*"
        
        ret += "\n"
        return ret
    
    def myclick(self):
        fir = self.le_first.text()
        ifir = int(fir)
        end = self.le_last.text()
        iend = int(end)
        
       # QPlainTextEdit().text => .setPlainText()
        
        txt = ""
        
        #txt += self.getStar(1)
        #txt += self.getStar(2)
        for i in range(ifir, iend+1):
            txt += self.getStar(i)
           
        self.pte.setPlainText(txt)

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    main_Window = UiMainWindow() 
    sys.exit(app.exec_())