from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt
import sys
from random import randint as r
from qq import Ui_MainWindow


class Main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = False

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag is True:
            x = r(0, 500)
            y = r(0, 600)
            l = r(0, 500)
            painter = QPainter(self)
            a = r(1, 5)
            if a == 1:
                painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            if a == 2:
                painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            if a == 3:
                painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            if a == 4:
                painter.setPen(QPen(Qt.purple, 5, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.purple, Qt.SolidPattern))
            if a == 5:
                painter.setPen(QPen(Qt.green, 5, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            painter.drawEllipse(x, y, l, l)
            self.flag = False


app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())