import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Painting(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.do_paint = False

        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.do_paint:
            self.draw(qp)
        qp.end()

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        radius = random.randint(1, self.width()) // 2
        x, y = random.randint(0, self.width() - radius), random.randint(0, self.height() - radius)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = Painting()
    ex.show()
    sys.exit(app.exec_())