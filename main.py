import sys
import random

from UI import Ui_Painting
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Painting(QMainWindow, Ui_Painting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        r, g, b = random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = Painting()
    ex.show()
    sys.exit(app.exec_())