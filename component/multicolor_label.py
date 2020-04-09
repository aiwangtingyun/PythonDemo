# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/03/25
import sys
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QFontMetrics, QFont, QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class MultcolorLabel(QWidget):

    def __init__(self, parent=None):
        super(MultcolorLabel, self).__init__(parent)
        self.resize(60, 20)
        self.text_items = []
        self.font = QFont('Microsoft YaHei')
        self.font.setPixelSize(14)
        self.font_metric = QFontMetrics(self.font)

        text = [
            {'content': '红色', 'color': '#ff0000'},
            {'content': '你好呀！', 'color': '#000000'},
            {'content': '绿色', 'color': '#00ff00'},
            {'content': '我很好！', 'color': '#000000'}
        ]
        self.set_text(text)

    def set_text(self, text):
        self.text_items = text
        self.update()

    def set_font_family(self, font_family):
        self.font.setFamily(font_family)
        self.font_metric = QFontMetrics(self.font)
        self.update()

    def set_font_size(self, size):
        self.font.setPixelSize(size)
        self.font_metric = QFontMetrics(self.font)
        self.update()

    def paintEvent(self, event):
        super(MultcolorLabel, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        pos_x = 0
        for item in self.text_items:
            content = item.get('content')
            color = item.get('color')
            text_len = self.font_metric.width(content)
            rect = QRect(pos_x, 0, text_len, self.height())
            painter.setFont(self.font)
            painter.setPen(QPen(QColor(color)))
            painter.setBrush(Qt.NoBrush)
            painter.drawText(rect, Qt.AlignCenter, content)
            pos_x += text_len


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Demo')
    window.resize(300, 100)
    window.label = MultcolorLabel(window)
    window.label.resize(200, 25)
    window.label.move((window.width()-window.label.width())//2, (window.height()-window.label.height())//2)
    window.show()

    sys.exit(app.exec_())
