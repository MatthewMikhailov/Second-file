import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            self.circle(painter)
            painter.end()

    def circle(self, painter):
        r = random.randint(10, 100)
        x = random.randint(50, 200)
        y = random.randint(50, 150)
        painter.setBrush(QColor('yellow'))
        painter.drawEllipse(x, y, 2 * r, 2 * r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())