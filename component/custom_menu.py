from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtGui import QFont, QFontMetrics, QPainter, QPainterPath, QBrush, QColor
from PyQt5.QtCore import Qt

class CustomMenu(QWidget):
    '''自定义菜单'''

    def __init__(self, parent=None):
        super(CustomMenu, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.Popup | Qt.NoDropShadowWindowHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.btn_list = []
        self.btn_height = 26
        self.resize(80, 35)
        self.addAction('菜单1')
        self.addAction('菜单选择2')
        self.addAction('菜单3')

    def addAction(self, text='', call_back=None):
        button = MenuButton(self, text)
        if call_back:
            button.clicked.connect(call_back)

        self.btn_list.append(button)
        for index, btn in enumerate(self.btn_list):
            btn.move(0, index * btn.height() + 11)
            if btn.width() > self.width():
                self.setFixedWidth(btn.width())
        for btn in self.btn_list:
            btn.setFixedWidth(self.width())
        self.setFixedHeight(11 + 3 + len(self.btn_list) * button.height())

    def clear(self):
        for btn in self.btn_list:
            btn.deleteLater()
        self.btn_list.clear()

    def paintEvent(self, event):
        '''重新绘制'''
        super(CustomMenu, self).paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        painter.setBrush(QBrush(QColor('#FFFFFF')))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 8, self.width(), self.height()-8, 6, 6)

        path = QPainterPath()
        path.moveTo(self.width()/2-8, 8)
        path.lineTo(self.width()/2, 0)
        path.lineTo(self.width()/2+8, 8)
        path.lineTo(self.width()/2-8, 8)
        painter.drawPath(path)

class MenuButton(QPushButton):
    def __init__(self, parent=None, text=''):
        super(MenuButton, self).__init__(parent)

        self.font = QFont('Microsoft YaHei')
        self.font.setPixelSize(14)
        self.font_metric = QFontMetrics(self.font)
        self.setText(text)
        pixel_len = self.font_metric.boundingRect(text).width() + 24 * 2
        self.resize(pixel_len, 26)
        self.setStyleSheet('''
            QPushButton{font-family:Microsoft YaHei; font-size:14px; color:#666666; border:none;  
                        background-color:#FFFFFF; text-align:left; padding-left:24px;}
            QPushButton:hover{background-color:#FF475D; color:#FFFFFF;}
        ''')