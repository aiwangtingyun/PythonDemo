#!/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import demjson

from PyQt5.QtQuickWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from center.config_center import get_style_sheet
from component.banner_widget import OpenNobilityBannerWidget, WorldBannerWidget
from component.chat_widget import ChatWidget
from component.circle_image import CircleImage
from component.image_scale import ImageScale
from component.movie_player import MoviePlayer


class MyWidget(QWidget):
    '''实现全透明窗口'''

    def __init__(self):
        super(MyWidget, self).__init__()

        # 去除背景
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # 窗口设置
        self.resize(500, 240)
        self.setWindowTitle('Test')
        # self.setObjectName('MyWidget')
        # self.setStyleSheet("QWidget#MyWidget{background:grey;}")

        self.button = QPushButton(self)
        self.button.setGeometry(100, 50, 120, 40)
        self.button.setText('右键按钮')

        self.mask = QWidget(self)
        self.mask.setGeometry(self.geometry())
        self.mask.setAttribute(Qt.WA_TransparentForMouseEvents)  # 鼠标穿透

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(0, 0, 200, 25)
        self.line_edit.setStyleSheet('''
            QLineEdit {background-color: blue; border: none; font-size: 12px;}
        ''')

        self.label = QLabel(self)
        self.label.setGeometry(0, 150, 300, 50)
        self.label.setText("134564")
        self.label.setStyleSheet("""
            QLabel{font: 16px "Microsoft YaHei"; color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFF857, stop:1 #FFD81E);}
        """)

        # self.load_qml()

    def load_qml(self):
        self.quck_view = QQuickWidget(self)
        self.quck_view.setSource(QUrl('./qmls/chat_room.qml'))
        self.quck_view.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self.quck_view.setGeometry(0, 0, self.width(), self.height())
        self.quck_view.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 测试样式表
    styleSheet = get_style_sheet('main.css')
    app.setStyleSheet(styleSheet)

    window = MyWidget()
    window.show()

    # 加载字体
    # font_path = os.path.join(ROOT_DIR, 'font/seguisym.ttf')
    # QFontDatabase.addApplicationFont(font_path)

    # 测试图片缩放
    # img_path = './image/tag_emperor.png'
    # img = QPixmap(img_path)
    # img = img.scaled(56, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    # img.save('./image/tag_emperor_1.png', 'png')

    # 测试聊天窗口
    # window = ChatWidget()
    # window.show()

    # 测试demjson
    # a = "{\"title\": \"\\u2605\\u6e29\\u99a8\\u63d0\\u793a\\u2605\", " \
    #     "\"content\": \"\\u6b22\\u8fce\\u6765\\u6253\\u6b4c\\u5385\\u623f\\n" \
    #     "\\ud83d\\ude04\\ud83d\\ude04\\ud83d\\ude04\\ud83d\\ude04\\ud83d\\ude03\", \"type\": 0}"
    # b = demjson.decode(a)
    # print(b)

    sys.exit(app.exec_())
