# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/03/16
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication


class CustomBackgrond(QWidget):
    '''自定义背景'''

    def __init__(self, parent=None):
        super(CustomBackgrond, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(311, 232)

    def paintEvent(self, event):
        super(CustomBackgrond, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # 绘制矩形背景
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor('#D4B8E3')))
        painter.drawRoundedRect(10, 50, self.width() - 20, self.height() - 54, 6, 6)

        # 绘制圆圈
        pen = QPen(QColor('#A683AF'))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawRoundedRect(123, 20, 64, 64, 32, 32)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = CustomBackgrond()
    widget.show()

    sys.exit(app.exec_())
