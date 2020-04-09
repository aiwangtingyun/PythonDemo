# -*- coding: utf-8 -*-
# @Author   : wangtingyun
# @Time     : 2020/03/28

import sys
from PyQt5.QtCore import QPropertyAnimation, Qt, QPoint, QEasingCurve, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class MarqueeWidget(QWidget):
    """跑马灯控件"""

    def __init__(self, parent):
        super(MarqueeWidget, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(200, 30)

        self.label_1 = QLabel(self)
        self.label_1.setGeometry(self.geometry())
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(self.geometry())

        self.duration = 4000
        self.spacing = 40

        self.anim_1 = QPropertyAnimation(self.label_1, b'pos')
        self.anim_1.setEasingCurve(QEasingCurve.Linear)
        self.anim_1.setDuration(self.duration)
        self.anim_1.setLoopCount(-1)
        self.anim_2 = QPropertyAnimation(self.label_2, b'pos')
        self.anim_2.setEasingCurve(QEasingCurve.Linear)
        self.anim_2.setDuration(self.duration)
        self.anim_2.setLoopCount(-1)

        self.init_ui()
        self.start_move()

    def init_ui(self):
        self.label_1.setStyleSheet("QLabel{font-family: 'Microsoft YaHei'; font-size: 14px; color: #000000;}")
        self.label_1.setText('欢迎来到房间这里是房间名字测试的房间')
        self.label_1.adjustSize()

        self.label_2.setStyleSheet(self.label_1.styleSheet())
        self.label_2.setText(self.label_1.text())
        self.label_2.adjustSize()

    def start_move(self):
        self.anim_1.setStartValue(QPoint(0, self.label_1.y()))
        self.anim_1.setEndValue(QPoint(-(self.label_1.width() + self.spacing), self.label_1.y()))

        self.anim_2.setStartValue(QPoint(self.label_1.width() + self.spacing, self.label_2.y()))
        self.anim_2.setEndValue(QPoint(0, self.label_2.y()))

        self.anim_1.start()
        self.anim_2.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Demo')
    window.resize(300, 100)
    window.label = MarqueeWidget(window)
    window.label.move((window.width()-window.label.width())//2, (window.height()-window.label.height())//2)
    window.show()

    sys.exit(app.exec_())
