import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.Qt import Qt, QMessageBox
from day06.mysql_insert3 import cnt
from tkinter import messagebox

form_class = uic.loadUiType("myomok03_19.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.flag_wb = True
        self.flag_over = False
        self.arr2d = [
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
        ]
        self.pb2d = []
        self.setupUi(self)
        
        for i in range(19):
            line = []
            for j in range(19):
                piece = QPushButton("", self)
                piece.setIcon(QIcon("0.png"))
                piece.setIconSize(QtCore.QSize(40, 40))
                piece.setGeometry(j*40, i*40, 40, 40)
                piece.setToolTip("{},{}".format(i, j))
                piece.clicked.connect(self.myclick)
                line.append(piece)
            self.pb2d.append(line)
            
        self.pb.clicked.connect(self.myreset)
            
        self.show()
        self.myrender()
        
    def myreset(self):
        #플래그 초기화, 2중 for문 arr2d => 0
        self.flag_wb = True
        self.flag_over = False
        
        for i in range(19) :
            for j in range(19) :
                self.arr2d[i][j] = 0
        
        self.myrender()
        
    def myrender(self):
        for i in range(19) :
            for j in range(19) :
                if self.arr2d[i][j] == 0 :
                    self.pb2d[i][j].setIcon(QIcon("0.png"))
                if self.arr2d[i][j] == 1 :
                    self.pb2d[i][j].setIcon(QIcon("1.png"))
                if self.arr2d[i][j] == 2 :
                    self.pb2d[i][j].setIcon(QIcon("2.png"))
        #self.pb2d[9][0].setIcon(QIcon("1.png"))
    
    # 방향1 = ul + dr + 1
    def getUP(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0 :
                    return cnt
                
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt  
        
    def getDW(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0 :
                    return cnt
                
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
        
    def getLE(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
        
    def getRI(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def getUR(self, i, j, stone):
            cnt = 0
            try:
                while True:
                    i -= 1
                    j += 1
                    if i < 0 :
                        return cnt
                    if j < 0 :
                        return cnt
                    
                    if self.arr2d[i][j] == stone :
                        cnt += 1
                    else :
                        return cnt
            except:
                return cnt        

    def getUL(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
        
    def getDL(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
    
    def getDR(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
        
    def myclick(self):
        if self.flag_over :
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2d[i][j] > 0 :
            return
        
        stone = -1
        if self.flag_wb :
            self.arr2d[i][j] = 1
            stone = 1
        else :
            self.arr2d[i][j] = 2
            stone = 2
            
        self.myrender()
        
        up = self.getUP(i, j, stone)
        dw = self.getDW(i, j, stone)
        le = self.getLE(i, j, stone)
        ri = self.getRI(i, j, stone)
        
        dr = self.getDR(i, j, stone)
        dl = self.getDL(i, j, stone)
        ur = self.getUR(i, j, stone)
        ul = self.getUL(i, j, stone)
        #print(up, dw, le, ri,  dr, dl, ur, ul)
        
        d1 = up + dw + 1
        d2 = le + ri + 1
        d3 = dl + ur + 1
        d4 = ul + dr + 1
        #print(d1, d2, d3, d4)
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            # if self.arr2d[i][j] = 1 :
            if self.flag_wb :
                QMessageBox.about(self, '오목', '흰돌 승리')
            else :
                QMessageBox.about(self, '오목', '흑돌 승리')
            self.flag_over = True
            
        self.flag_wb = not self.flag_wb
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()