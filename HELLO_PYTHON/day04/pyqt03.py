from PyQt5 import QtWidgets, uic
import sys

form_window = uic.loadUiType("pyqt03.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        a = int(self.te01.toPlainText())
        b = int(self.te02.toPlainText())
        c = a * b
        self.te03.setText(str(c))
        
if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    main_Window = UiMainWindow() 
    sys.exit(app.exec_())