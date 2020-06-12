import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QPainterPath, QLinearGradient
from PyQt5.QtWidgets import QWidget, QApplication


class TipLabel(QWidget):
    def __init__(self, parent=None):
        super(TipLabel, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(233, 26)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        linear_gradient = QLinearGradient(0, 0, self.width(), 0)
        linear_gradient.setColorAt(0, QColor('#FF48ED'))
        linear_gradient.setColorAt(1, QColor('#43A2FF'))
        brush = QBrush(linear_gradient)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        # 绘制弧形框
        painter.drawRoundedRect(0, 6, 233, 20, 10, 10)

        # 绘制上三角
        path = QPainterPath()
        path.moveTo(18, 6)
        path.lineTo(24, 0)
        path.lineTo(30, 6)
        painter.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = TipLabel()
    widget.show()

    sys.exit(app.exec_())
