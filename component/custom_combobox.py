# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CustomComboBox(QWidget):
    def __init__(self):
        super(CustomComboBox, self).__init__()
        self.resize(320, 240)

        self.edit = QLineEdit(self)
        self.edit.setGeometry(50, 50, 150, 30)
        self.edit.setStyleSheet("""
            QLineEdit {padding-left:30px; padding-right:20px;}
        """)

        self.dropButton = QPushButton(self)
        self.dropButton.setGeometry(199, 49, 32, 32)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20.0)
        self.shadow.setOffset(5.0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(50, 80, 180, 100)
        self.listWidget.hide()
        self.listWidget.setStyleSheet("""
            QListWidget{background-color:#151921;border:none;outline:none;border-radius:4px;}
            QListWidget::item{height:30px;border:none;padding:0px;background:transparent;}
        """)
        self.listWidget.setGraphicsEffect(self.shadow)

        self.edit.installEventFilter(self)
        self.dropButton.installEventFilter(self)
        self.installEventFilter(self)

        for i in range(4):
            self.addItem("1342811926%d" % i)

    def showMenu(self):
        if self.listWidget.isHidden():
            self.listWidget.show()
        else:
            self.listWidget.hide()

    def addItem(self, name):
        item = QListWidgetItem('')
        item_widget = itemWidget(name, self.listWidget.count())
        item_widget.itemClicked.connect(self.setText)
        item_widget.deleteSignal.connect(self.deleteItem)
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, item_widget)
        self.listWidget.resize(self.listWidget.width(), self.listWidget.count()*item_widget.height())

    def setText(self, text):
        self.edit.setText(text)
        self.listWidget.hide()

    def deleteItem(self, index):
        print("删除了第%d个账号" % index)
        self.listWidget.hide()

    def eventFilter(self, obj, event):
        if obj == self:
            if event.type() == QEvent.MouseButtonPress:
                self.listWidget.hide()
                return False
        elif obj == self.dropButton:
            if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self.showMenu()
                return False
        elif obj == self.edit:
            if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self.listWidget.hide()
                return False
        return False

class itemWidget(QWidget):
    deleteSignal = pyqtSignal(int)
    itemClicked = pyqtSignal(str)

    def __init__(self, name, index):
        super(itemWidget, self).__init__()
        self.setAttribute(Qt.WA_Hover)
        self.resize(180, 30)
        self.index = index

        # 显示文本标签
        self.textLabel = QLabel(self)
        self.textLabel.setText(name)
        self.textLabel.setGeometry(0, 0, 150, 20)
        self.textLabel.setStyleSheet("""
            QLabel{font-family:'Microsoft YaHei'; font-size:12px; color:#BDC8E2; background:transparent;
                    padding-left:6px; padding-top:10px;}
            QLabel:hover{color:#66CDFF;}
        """)

        # 删除按钮
        self.deleteButton = QPushButton(self)
        self.deleteButton.setGeometry(150, 5, 30, 20)
        self.deleteButton.hide()
        self.deleteButton.setStyleSheet("""
            QPushButton{background: url(./image/delete_hover) center center no-repeat; background-color:transparent; border:none;}
            QPushButton:pressed{background: url(./image/delete_pressed) center center no-repeat;}
        """)

        # 监听事件
        self.textLabel.installEventFilter(self)
        self.deleteButton.installEventFilter(self)
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self:
            if event.type() == QEvent.HoverEnter:
                self.deleteButton.show()
                return True
            elif event.type() == QEvent.HoverLeave:
                self.deleteButton.hide()
                return True
        elif obj == self.textLabel:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.itemClicked.emit(self.textLabel.text())
                return True
        elif obj == self.deleteButton:
            if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self.deleteSignal.emit(self.index)
                return True
        return False