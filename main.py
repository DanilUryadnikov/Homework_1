from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSizes(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 340, 151, 171))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Окружности"))


class round(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ul.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.l = []
        self.color = []

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_flag(self.qp)
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        d = random.randint(30, 200)
        x = random.randint(50, 600)
        y = random.randint(50, 600)
        color1 = random.randint(0, 256)
        color2 = random.randint(0, 256)
        color3 = random.randint(0, 256)
        self.l.append([x, y, d])
        self.color.append((color1, color2, color3))
        for i in range(len(self.l)):
            self.qp.setBrush(QColor(self.color[i][0], self.color[i][1], self.color[i][2]))
            self.qp.drawEllipse(self.l[i][0], self.l[i][1], self.l[i][2], self.l[i][2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = round()
    ex.show()
    sys.exit(app.exec_())
