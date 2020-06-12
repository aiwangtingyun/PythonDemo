# -*- coding: utf-8 -*-
# @Authon   : wangtingyun
# @Time     : 2020/03/12

import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication


class CircleImage(QWidget):
    '''绘制圆形图片'''

    def __init__(self, parent=None):
        super(CircleImage, self).__init__(parent)

        # 移除背景
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(100, 100)
        self.circle_image = None

    def set_image(self, image):
        '''设置绘制的图片'''
        self.circle_image = image
        self.update()

    def paintEvent(self, event):
        '''重写绘制事件'''
        super(CircleImage, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)  # 设置抗锯齿
        pen = QPen(QColor('#ff0000'))                       # 设置边框颜色
        pen.setWidth(2)                                     # 设置边框宽度
        painter.setPen(pen)                                 # 添加描边边框
        brush = QBrush(self.circle_image)                   # 添加绘制内容
        painter.setBrush(brush)

        rect = QRect(2, 2, self.width() - 4, self.height() - 4)
        painter.drawRoundedRect(rect, self.width() / 2, self.height() / 2)


if __name__ == '__main__':
    # 控件测试程序
    app = QApplication(sys.argv)

    widget = CircleImage()
    image = QPixmap('../images/girl.jpg')
    widget.set_image(image.scaled(widget.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    widget.show()

    sys.exit(app.exec_())
