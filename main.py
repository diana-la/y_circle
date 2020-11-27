import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('ui.ui', self)
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)

    def paint(self):
        self.do_paint = True
        self.repaint()  # перерисовываем

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        h = random.randint(0, 580)  # ширина и высота
        x = random.randint(0, 580)  # расположение по х
        y = random.randint(0, 580)  # расположение по у
        qp.drawEllipse(x, y, h, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
