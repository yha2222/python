from PyQt5 import QtWidgets, uic, QtGui
import sys
from PyQt5.Qt import QLabel, Qt

form_window = uic.loadUiType("myomok01.ui")[0]

class UiMainWindow(QtWidgets.QMainWindow, form_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # self. 붙여서 전역변수화 -> 함수 2개 따로 씀 => 별로
        # self.label1 = QLabel('First Label', self)
        # self.label1.setGeometry(0, 0, 40, 40)
        # self.label1.setPixmap(QtGui.QPixmap("0.png"))
        # self.label1.mousePressEvent = self.click2
        
        self.pb.clicked.connect(self.myclick)
        self.show()
        
        #self.lbl.mousePressEvent = self.click
        
    def myclick(self, event):
        #self.pb = self.sender()
        self.sender().setIcon(QtGui.QIcon('1.png'))
        
        #self.lbl.setPixmap(QtGui.QPixmap("1.png"))
    # def click2(self, event):
    #     self.label1.setPixmap(QtGui.QPixmap("1.png"))

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    main_window = UiMainWindow() 
    sys.exit(app.exec_())