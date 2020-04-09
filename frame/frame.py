# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class borderFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.ToolTip | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("#00BBF4"))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRect(1, 1, self.width()-2, self.height()-2)

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.resize(640, 480)
        self.titleBar = QWidget(self)
        self.titleBar.setGeometry(0, 0, self.width(), 35)
        self.titleBar.setStyleSheet("QWidget{background-color:#212735;}")
        self.setStyleSheet("QWidget{background:#151921;border-width:1px;border-color:#00BBF4;border-style:solid;}")
        self.titleBar.installEventFilter(self)
        self.buttonPressed = False
        self.startPos = None
        self.pressedType = ""
        self.move(600, 300)
        self.installEventFilter(self)

        self.closeButton = QPushButton(self)
        self.closeButton.setGeometry(self.width()-32, 9, 19, 15)
        self.closeButton.setStyleSheet("QPushButton{background-image:url(./image1.png); border:none; background-color:transparent;}")
        self.closeButton.clicked.connect(self.close)

        self.moveBorder = borderFrame()
        self.moveBorder.setGeometry(self.x(), self.y(), self.width(), self.height())
        self.moveBorder.setMinimumSize(640, 480)
        self.moveBorder.hide()

    def paint(self):
        painter = QPainter(self)
        pen = QPen(QColor("#00BBF4"))
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawRect(0, 0, self.width()-1, self.height()-1)

    def moveWidget(self, pos):
        self.moveBorder.show()
        self.moveBorder.move(self.moveBorder.pos() + pos)

    def resizeWidget(self, movePos, mousePos):
        self.moveBorder.show()
        resizeWidth = 0
        resizeHeight = 0
        if self.pressedType == "left":
            self.moveBorder.setGeometry(mousePos.x(), self.moveBorder.y(), self.moveBorder.width()-movePos.x(), \
                                        self.moveBorder.height())
        elif self.pressedType == "top":
            self.moveBorder.setGeometry(self.moveBorder.x(), mousePos.y(), self.moveBorder.width(), \
                                        self.moveBorder.height()-movePos.y())
        elif self.pressedType == "right":
            resizeWidth = self.moveBorder.width()+movePos.x()
            resizeHeight = self.moveBorder.height()
            print("=========", mousePos.x(),"==========", self.moveBorder.x()+self.moveBorder.minimumWidth())
            if mousePos.x() > self.moveBorder.x()+self.moveBorder.minimumWidth():
                self.moveBorder.setGeometry(self.moveBorder.x(), self.moveBorder.y(), resizeWidth, resizeHeight)
        elif self.pressedType == "bottom":
            self.moveBorder.setGeometry(self.moveBorder.x(), self.moveBorder.y(), self.moveBorder.width(), \
                                        self.moveBorder.height()+movePos.y())
        elif self.pressedType == "leftTop":
            self.moveBorder.setGeometry(mousePos.x(), mousePos.y(), self.moveBorder.width()-movePos.x(), \
                                        self.moveBorder.height() - movePos.y())
        elif self.pressedType == "leftBottom":
            self.moveBorder.setGeometry(mousePos.x(), self.moveBorder.y(), self.moveBorder.width()-movePos.x(), \
                                        self.moveBorder.height() + movePos.y())
        elif self.pressedType == "rightTop":
            self.moveBorder.setGeometry(self.moveBorder.x(), self.moveBorder.y()+movePos.y(), self.moveBorder.width()+movePos.x(),\
                                        self.moveBorder.height()-movePos.y())
        elif self.pressedType == "rightBottom":
            resizeWidth = self.moveBorder.width()+movePos.x()
            resizeHeight = self.moveBorder.height()+movePos.y()
            self.moveBorder.setGeometry(self.moveBorder.x(), self.moveBorder.y(), resizeWidth, resizeHeight)

    def releaseWidget(self):
        self.moveBorder.hide()
        self.setGeometry(self.moveBorder.x(), self.moveBorder.y(), self.moveBorder.width(), self.moveBorder.height())
        self.titleBar.setGeometry(0, 0, self.width(), 30)
        self.closeButton.setGeometry(self.width()-29, 7, 19, 15)

    def updateMouseShape(self, pos):
        width = 5
        topBorder = QRect(width, 0, self.width()-width*2, width)
        bottomBorder = QRect(width, self.height()-width, self.width()-width*2, width)
        leftBorder = QRect(0, width, width, self.height()-width*2)
        rightBorder = QRect(self.width()-width, width, width, self.height()-width*2)
        leftTopBorder = QRect(0, 0, width, width)
        rightTopBorder = QRect(self.width()-width, 0, width, width)
        leftBottomBorder = QRect(0, self.height()-width, width, width)
        rightBottomBorder = QRect(self.width()-width, self.height()-width, width, width)

        if pos in topBorder:
            self.setCursor(Qt.SizeVerCursor)
            self.pressedType = "top"
        elif pos in bottomBorder:
            self.setCursor(Qt.SizeVerCursor)
            self.pressedType = "bottom"
        elif pos in leftBorder:
            self.setCursor(Qt.SizeHorCursor)
            self.pressedType = "left"
        elif pos in rightBorder:
            self.setCursor(Qt.SizeHorCursor)
            self.pressedType = "right"
        elif pos in leftTopBorder:
            self.setCursor(Qt.SizeFDiagCursor)
            self.pressedType = "leftTop"
        elif pos in rightBottomBorder:
            self.setCursor(Qt.SizeFDiagCursor)
            self.pressedType = "rightBottom"
        elif pos in rightTopBorder:
            self.setCursor(Qt.SizeBDiagCursor)
            self.pressedType = "rightTop"
        elif pos in leftBottomBorder:
            self.setCursor(Qt.SizeBDiagCursor)
            self.pressedType = "leftBottom"
        else:
            self.pressedType = ""
            self.setCursor(Qt.ArrowCursor)

    def eventFilter(self, obj, event):
        if obj == self.titleBar:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.buttonPressed = True
                self.startPos = event.globalPos()
            elif event.type() == QEvent.MouseMove and self.buttonPressed:
                movePos = event.globalPos() - self.startPos
                if self.cursor() == Qt.ArrowCursor:
                    self.moveWidget(movePos)
                else:
                    self.resizeWidget(movePos, event.globalPos())
                self.startPos = event.globalPos()
            elif event.type() == QEvent.MouseButtonRelease and self.buttonPressed:
                self.releaseWidget()
                self.buttonPressed = False
            return True
        elif obj == self:
            if event.type() == QEvent.HoverMove and not self.buttonPressed:
                self.updateMouseShape(event.pos())
            elif event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                if self.cursor() != Qt.ArrowCursor:
                    self.buttonPressed = True
                    self.startPos = event.globalPos()
            elif event.type() == QEvent.MouseMove and self.buttonPressed:
                movePos = event.globalPos() - self.startPos
                self.resizeWidget(movePos, event.globalPos())
                self.startPos = event.globalPos()
            elif event.type() == QEvent.MouseButtonRelease and self.buttonPressed:
                self.releaseWidget()
                self.buttonPressed = False
            elif event.type() == QEvent.Paint:
                self.paint()
            return True
        return True
