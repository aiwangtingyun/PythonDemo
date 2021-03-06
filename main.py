#!/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtQuickWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from center.config_center import get_style_sheet, ROOT_DIR
from component.emoji_widget import EmojiWidget


class WidgetDemo(QWidget):
    """ 实现全透明窗口 """

    def __init__(self):
        super(WidgetDemo, self).__init__()

        # 去除背景
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # 窗口设置
        self.resize(240, 120)
        self.setWindowTitle('window')
        # self.setObjectName('MyWidget')
        # self.setStyleSheet("QWidget#MyWidget{background:grey;}")

        self.combobox = QComboBox(self)
        self.combobox.resize(130, 36)
        self.combobox.move((self.width() - self.combobox.width()) // 2, (self.height() - self.combobox.height()) // 2)
        self.combobox.setStyleSheet(get_style_sheet('combobox.css', 'qt'))
        self.combobox.addItem('item1')
        self.combobox.addItem('item2')
        self.combobox.addItem('item3')

        # self.button = QPushButton(self)
        # self.button.setGeometry(100, 50, 120, 40)
        # self.button.setText('右键按钮')

        # self.load_qml()

    def leaveEvent(self, event):
        print(self.__class__.__name__)

    def load_qml(self):
        self.quck_view = QQuickWidget(self)
        self.quck_view.setSource(QUrl('./qmls/chat_room.qml'))
        self.quck_view.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self.quck_view.setGeometry(0, 0, self.width(), self.height())
        self.quck_view.show()


class TestWidget(WidgetDemo):
    def __init__(self):
        super(TestWidget, self).__init__()


def load_font():
    # 加载字体
    font_path = os.path.join(ROOT_DIR, 'font/seguisym.ttf')
    QFontDatabase.addApplicationFont(font_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = EmojiWidget()
    widget.show()

    sys.exit(app.exec_())
