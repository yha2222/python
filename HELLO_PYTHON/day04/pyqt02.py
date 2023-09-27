from PyQt5 import QtWidgets, uic
import sys

form_window = uic.loadUiType("pyqt02.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        self.DECREASE.clicked.connect(self.myclick)
    def myclick(self):
        a = self.lineEdit.text()
        aa = int(a)
        aa -= 1
        self.lineEdit.setText(str(aa))
        
if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    main_Window = UiMainWindow() 
    sys.exit(app.exec_())