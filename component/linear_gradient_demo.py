# -*- coding: utf-8 -*-
# @Time    : 2020/05/26
# @Author  : wangtingyun

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QLinearGradient, QFont, QBrush, QColor, QPen, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication


class LinearGradientWidget(QWidget):
    """
    绘制渐变颜色背景的控件
    """
    def __init__(self, parent=None):
        super(LinearGradientWidget, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(300, 40)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)

        # 绘制渐变圆角背景
        linear_gradient = QLinearGradient(0, 0, self.width(), 0)
        linear_gradient.setColorAt(0, QColor('#FF132F'))
        linear_gradient.setColorAt(1, QColor('#0079FF'))
        painter.setPen(Qt.NoPen)
        painter.setBrush(linear_gradient)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height()//2, self.height()//2)

        # 左上角更改为小圆角
        painter.drawRoundedRect(0, 0, self.height()//2, self.height()//2, 4, 4)

        # 绘制文字
        font = QFont('微软雅黑')
        font.setPixelSize(18)
        painter.setFont(font)
        painter.setPen(QPen(QColor('#FFFDD4')))
        painter.setBrush(Qt.NoBrush)
        painter.drawText(self.rect(), Qt.AlignCenter, '绘制渐变背景')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = LinearGradientWidget()
    widget.show()

    sys.exit(app.exec_())
