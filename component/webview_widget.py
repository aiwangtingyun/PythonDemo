# -*- coding: utf-8 -*-
# @Time    : 2020/01/02
# @Author  : wangtingyun

import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView


class WebViewWidget(QWidget):

    def __init__(self, parent=None):
        super(WebViewWidget, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet('QWidget{background: transparent;}')
        self.web_view = QWebEngineView(self)
        self.web_view.setAttribute(Qt.WA_TranslucentBackground)
        self.web_view.setStyleSheet('background: transparent;')
        self.web_view.page().setBackgroundColor(Qt.transparent)
        self.set_url()

    def resizeEvent(self, event):
        self.web_view.setGeometry(self.geometry())

    def set_url(self):
        self.web_view.load(QUrl('https://res11-aipai-pic.weplay.cn/nobility/nobility_horse_emperor_ani.webp'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    # window.setWindowFlags(window.windowFlags() | Qt.FramelessWindowHint)
    # window.setAttribute(Qt.WA_TranslucentBackground)
    window.setWindowTitle('Demo')
    window.resize(750, 520)

    window.webview = WebViewWidget(window)
    window.webview.setGeometry(window.geometry())

    window.show()

    sys.exit(app.exec_())
