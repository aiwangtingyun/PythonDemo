# -*- coding: utf-8 -*-
# @Time     : 2019-04-25
# @Author   : wangtingyun
# @Email    : wty1793172997@163.com

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton

from frame.frame import MoveFrame


class MessageDialog(QDialog):
    def __init__(self, parent=None, title="提示", message="请输入提示信息！"):
        super(MessageDialog, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setModal(True)
        self.moveFrame = MoveFrame()
        self.parent = parent
        self.title = title
        self.message = "<p align=\"center\">" + message
        self.initUI()
        self.connectSlot()

    def initUI(self):
        # 窗口
        self.setFixedSize(360, 240)
        self.setObjectName("message_dialog")
        self.initLocation()
        # 组件
        self.widget_titleBar = QWidget(self)
        self.widget_titleBar.setGeometry(0, 0, self.width(), 30)
        self.widget_titleBar.setObjectName("widget_titleBar")
        self.widget_titleBar.installEventFilter(self)
        self.widget_body = QWidget(self)
        self.widget_body.setGeometry(0, 30, self.width(), self.height()-30)
        self.widget_body.setObjectName("dialog_body")
        # 标签
        self.label_title = QLabel(self.widget_titleBar)
        self.label_title.setObjectName("label_title")
        self.label_title.setGeometry(6, 0, 50, 30)
        self.label_title.setText(self.title)
        self.label_icon = QLabel(self.widget_body)
        self.label_icon.setObjectName("label_dialog_image")
        self.label_icon.setGeometry(self.width()/2-50, 15, 90, 90)
        self.label_message = QLabel(self.widget_body)
        self.label_message.setObjectName("label_message")
        self.label_message.setGeometry(0, 118, self.width(), 30)
        self.label_message.setText(self.message)
        # 按钮
        self.pushButton_close = QPushButton(self.widget_titleBar)
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_close.setGeometry(335, 5, 18, 18)
        self.pushButton_ok = QPushButton(self.widget_body)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_ok.setGeometry(self.width()/2-80, self.label_message.y()+45, 160, 35)
        self.pushButton_ok.setText("确定")

    def initLocation(self):
        if self.parent:
            desktopWidth = QApplication.desktop().availableGeometry().width()
            desktopHeight = QApplication.desktop().availableGeometry().height()
            # 确定x坐标
            x = self.parent.x() + self.parent.width()/2 - self.width()/2
            if x < 0: x = 0
            elif x + self.width() > desktopWidth: x = desktopWidth - self.width()
            # 确定y坐标
            y = self.parent.y() + self.parent.height()/2 - self.height()/2
            if y < 0: y = 0
            elif y + self.height() > desktopHeight: y = desktopHeight - self.height()
            # 设置弹窗位置
            self.setGeometry(x, y, self.width(), self.height())

    def connectSlot(self):
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_ok.clicked.connect(self.close)

    def eventFilter(self, obj, event):
        if obj == self.widget_titleBar:
            self.moveFrame.eventFilter(self, event)

        return False
