# -*- coding: utf-8 -*-
# @Time    : 2020/01/09
# @Author  : wangtingyun
# @Email   : wangtingyun@aipai.com

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton


class NewMsgTipButton(QWidget):
    button_clicked = pyqtSignal()

    def __init__(self, parent=None, width=100, height=30):
        super(NewMsgTipButton, self).__init__(parent)
        self.resize(width, height)
        self.setAttribute(Qt.WA_StyledBackground)   # 使qss背景图片样式生效

        self.label_count = QLabel(self)
        self.label_down_icon = QLabel(self)
        self.button = QPushButton(self)

        self.init_ui()
        self.init_connect()

    def init_ui(self):
        self.setStyleSheet('QWidget{background: url(./image/new_msg.png) center no-repeat transparent; '
                           'border:none; font-family: "Microsoft YaHei"; font-size:12px;}')

        self.label_count.setAlignment(Qt.AlignCenter)
        self.label_count.setGeometry(9, 4, 16, 20)
        self.label_count.setStyleSheet('QLabel{background: transparent; color: #FF8B00;}')

        self.label_down_icon.setGeometry(80, 9, 6, 9)
        self.label_down_icon.setStyleSheet('QLabel{background:url(./image/dropdown.png) center no-repeat;'
                                           'background-color:transparent;}')

        self.button.setCursor(Qt.PointingHandCursor)
        self.button.setGeometry(self.geometry())
        self.button.setText('条新消息')
        self.button.setStyleSheet('QPushButton{background: transparent; color:#cf000000; padding-bottom:2px;}')

    def init_connect(self):
        self.button.clicked.connect(self.button_clicked.emit)

    def set_msg_count(self, count):
        self.label_count.setText('%d' % count)
