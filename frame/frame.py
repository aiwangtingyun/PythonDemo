# -*- coding: utf-8 -*-
# @Time     : 2019-03-18
# @Author   : wangtingyun
# @Email    : wty1793172997@163.com

from PyQt5.QtCore import QEvent, Qt, QRect
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QCursor

# import win32api, win32con

TOP, BOTTOM, LEFT, RIGHT, TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT = range(8)


class FrameBorder(QWidget):
    """ 边框 """
    def __init__(self):
        super(FrameBorder, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.ToolTip|Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        pen = QPen(QColor("#009ade"))
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawRect(self.geometry().x(), self.geometry().y(), self.width()-1, self.height()-1)


class MoveFrame(object):
    """ 移动框架 """
    def __init__(self, doubleClicked=False):
        self.startPos = None
        self.doubleClicked = doubleClicked
        # self.screenHeight = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        self.desktop = QApplication.desktop()
        self.validGeometry = self.desktop.availableGeometry()

    def eventFilter(self, window, event):
        if event.type() == QEvent.MouseButtonDblClick and self.doubleClicked:
            if window.cursor().shape() == Qt.ArrowCursor:
                window.onMaxClicked()
        elif window.isMaximized():
            if event.type() == QEvent.MouseButtonPress:
                self.startPos = event.globalPos()
            elif event.type() == QEvent.MouseMove and self.startPos:
                ratial = event.globalX() / window.width()
                x = event.globalX() - ratial * window.normalSize.width()
                window.onMaxClicked()
                window.setGeometry(x, event.globalPos().y()-10, window.normalSize.width(), window.normalSize.height())
            elif event.type() == QEvent.MouseButtonRelease:
                self.startPos = None
        elif not window.isMaximized():
            # event.globalPos()返回的是相对于屏幕的坐标
            if event.type() == QEvent.MouseButtonPress:
                self.startPos = event.globalPos()
            elif event.type() == QEvent.MouseMove:
                if self.startPos and window.cursor().shape() == Qt.ArrowCursor:
                    movePos = event.globalPos() - self.startPos
                    if window.y() > self.validGeometry.height()-50 and movePos.y() > 0:
                        return
                    window.move(window.pos() + movePos)
                    self.startPos = event.globalPos()
            elif event.type() == QEvent.MouseButtonRelease:
                self.startPos = None


class ResizeFrame(object):
    """ 缩放框架 """
    def __init__(self, border = 5):
        self.border = border
        self.startPos = None
        self.mouseLoc = None

    # 获取鼠标形状
    def getCursorShape(self, pos, w, h):
        # 设定边框范围
        rect_top = QRect(self.border, 0, w-(2*self.border), self.border)
        rect_bottom = QRect(self.border, h-self.border, w-(2*self.border), self.border)
        rect_left = QRect(0, self.border, self.border, h-(2*self.border))
        rect_right = QRect(w-self.border, self.border, self.border, h-(2*self.border))
        rect_topLeft = QRect(0, 0, self.border, self.border)
        rect_bottomRight = QRect(w-self.border, h-self.border, self.border, self.border)
        rect_topRight = QRect(w-self.border, 0, self.border, self.border)
        rect_bottomLeft = QRect(0, h-self.border, self.border, self.border)
        # 设定鼠标形状
        if rect_right.contains(pos):
            self.mouseLoc = RIGHT
            return QCursor(Qt.SizeHorCursor)
        # elif rect_left.contains(pos):
        #     self.mouseLoc = LEFT
        #     return QCursor(Qt.SizeHorCursor)
        # elif rect_top.contains(pos):
        #     self.mouseLoc = TOP
        #     return QCursor(Qt.SizeVerCursor)
        elif rect_bottom.contains(pos):
            self.mouseLoc = BOTTOM
            return QCursor(Qt.SizeVerCursor)
        # elif rect_topLeft.contains(pos):
        #     self.mouseLoc = TOP_LEFT
        #     return QCursor(Qt.SizeFDiagCursor)
        elif rect_bottomRight.contains(pos):
            self.mouseLoc = BOTTOM_RIGHT
            return QCursor(Qt.SizeFDiagCursor)
        # elif rect_topRight.contains(pos):
        #     self.mouseLoc = TOP_RIGHT
        #     return QCursor(Qt.SizeBDiagCursor)
        # elif rect_bottomLeft.contains(pos):
        #     self.mouseLoc = BOTTOM_LEFT
        #     return QCursor(Qt.SizeBDiagCursor)

        self.mouseLoc = None
        return QCursor(Qt.ArrowCursor)

    # 绘制窗口大小
    def getGeometryRect(self, movePos, geometry):
        rect = QRect(geometry)
        if self.mouseLoc == LEFT:
            rect.setLeft(rect.left() + movePos.x())
        elif self.mouseLoc == RIGHT:
            rect.setRight(rect.right() + movePos.x())
        elif self.mouseLoc == TOP:
            rect.setTop(rect.top() + movePos.y())
        elif self.mouseLoc == BOTTOM:
            rect.setBottom(rect.bottom() + movePos.y())
        elif self.mouseLoc == TOP_LEFT:
            rect.setTopLeft(rect.topLeft() + movePos)
        elif self.mouseLoc == TOP_RIGHT:
            rect.setTopRight(rect.topRight() + movePos)
        elif self.mouseLoc == BOTTOM_LEFT:
            rect.setBottomLeft(rect.bottomLeft() +  movePos)
        elif self.mouseLoc == BOTTOM_RIGHT:
            rect.setBottomRight(rect.bottomRight() + movePos)
        return rect

    def eventFilter(self, window, event):
        if event.type() == QEvent.HoverMove:
            # event.pos()返回的是相对于窗口的坐标
            cursor = self.getCursorShape(event.pos(), window.width(), window.height())
            window.setCursor(cursor)
        elif event.type() == QEvent.MouseButtonPress:
            self.startPos = event.globalPos()
        elif event.type() == QEvent.MouseMove:
            if self.startPos and self.mouseLoc:
                movePos = event.globalPos() - self.startPos
                rect = self.getGeometryRect(movePos, window.geometry())
                window.setGeometry(rect)
                self.startPos = event.globalPos()
                window.normalSize.setWidth(rect.width())
                window.normalSize.setHeight(rect.height())
        elif event.type() == QEvent.MouseButtonRelease:
            self.startPos = None