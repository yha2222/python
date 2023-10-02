from PyQt5 import QtWidgets, uic
import sys
from PyQt5.Qt import QMessageBox

form_window = uic.loadUiType("pyqt06.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        
        self.pb_call.clicked.connect(self.mycall)
    def mycall(self):
        str_tel = self.le.text()
        QMessageBox.about(self,'calling...',str_tel)
        
    def myclick(self):
        str_new = self.sender().text()
        str_old = self.le.text()
        #print(str_new, str_old)
        self.le.setText(str_old + str_new)
        
if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    main_Window = UiMainWindow() 
    sys.exit(app.exec_())