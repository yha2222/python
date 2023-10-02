from PyQt5 import QtWidgets, uic
import sys

form_window = uic.loadUiType("pyqt05.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        dan = self.le.text()
        idan = int(dan)
        t = ''
        
        for i in range(1, 9+1) :
            t += "{} * {} = {} \n".format(dan, i, idan*i)
        
        self.te.setPlainText(t)
if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    main_Window = UiMainWindow() 
    sys.exit(app.exec_())