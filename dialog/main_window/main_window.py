# -*- coding: utf-8 -*-
# @Time     : 2019-03-11
# @Author   : wangtingyun
# @Email    : wty1793172997@163.com

import os
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt, QEvent, QUrl
from PyQt5.QtWidgets import QPushButton, QShortcut
from PyQt5.QtGui import QKeySequence

from component.stylesheet import ICON_SHOWMAX, ICON_SHOWNORMAL, INPUT_URL, LEAVE_URL
from dialog.main_window.ui.main_window import Ui_main_window
from dialog.message_dialog import MessageDialog
from frame.frame import MoveFrame, ResizeFrame


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_Hover)  # 使能QEvent.HoverMove
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.moveFrame = MoveFrame(True)
        self.resizeFrame = ResizeFrame()
        self.defaultUrlText = "使用 百度 搜索，或者输入网址"
        self.curUrl = QUrl("https://www.baidu.com")
        self.initUI()
        self.initShortcut()
        self.normalSize = self.size()

        self.connectSlot()

    def initUI(self):
        self.initLineEdit()
        self.initLoacation()
        self.setMinimumSize(640, 480)
        self.layout().setContentsMargins(1, 1, 1, 1)
        self.ui.label_appName.setText("TotalBrowser")
        self.ui.pushButton_back.setCursor(Qt.PointingHandCursor)
        self.ui.pushButton_forward.setCursor(Qt.PointingHandCursor)
        self.ui.pushButton_menu.setCursor(Qt.PointingHandCursor)
        self.ui.pushButton_home.setCursor(Qt.PointingHandCursor)
        self.ui.pushButton_refresh.setCursor(Qt.PointingHandCursor)
        self.ui.pushButton_min.setCursor(Qt.PointingHandCursor)
        self.ui.pushButton_max.setCursor(Qt.PointingHandCursor)
        self.ui.pushButton_close.setCursor(Qt.PointingHandCursor)
        self.ui.pushButton_bookmark.setCursor(Qt.PointingHandCursor)
        self.ui.pushButton_slidebar.setCursor(Qt.PointingHandCursor)
        self.ui.widget_webView.load(self.curUrl)
        self.ui.label_logo.setText("")

        # 安装事件过滤器
        self.installEventFilter(self)
        self.ui.widget_titleBar.installEventFilter(self)
        self.ui.lineEdit_url.installEventFilter(self)

    def initLoacation(self):
        desktop = QApplication.desktop()
        desktopWidth = desktop.availableGeometry().width()
        desktopHeight = desktop.availableGeometry().height()
        self.setGeometry(250, 100, desktopWidth-500, desktopHeight-200)

    def initShortcut(self):
        # 刷新快捷键
        self.refreshShortcut = QShortcut(QKeySequence("F5"), self)
        self.refreshShortcut.activated.connect(self.onRefreshClicked)
        # 前进快捷键
        self.forwordShorcut = QShortcut(QKeySequence("Alt+Right"), self)
        self.forwordShorcut.activated.connect(self.onForwardClicked)
        # 后退快捷键
        self.backwordShorcut = QShortcut(QKeySequence("Alt+Left"), self)
        self.backwordShorcut.activated.connect(self.onBackwardClicked)

    def connectSlot(self):
        self.ui.pushButton_min.clicked.connect(self.showMinimized)
        self.ui.pushButton_max.clicked.connect(self.onMaxClicked)
        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.pushButton_refresh.clicked.connect(self.onRefreshClicked)
        self.ui.pushButton_forward.clicked.connect(self.onForwardClicked)
        self.ui.pushButton_back.clicked.connect(self.onBackwardClicked)
        self.ui.pushButton_menu.clicked.connect(self.onMenuClicked)
        self.ui.pushButton_home.clicked.connect(self.onHomePageClicked)
        self.ui.pushButton_bookmark.clicked.connect(self.onBookmarkClicked)
        self.ui.pushButton_slidebar.clicked.connect(self.onSlidebarClicked)
        self.ui.widget_webView.loadStarted.connect(self.onLoadStart)
        self.ui.widget_webView.loadProgress.connect(self.onLoadProgress)
        self.ui.widget_webView.loadFinished.connect(self.onLoadFinish)

    # 重构网址输入栏样式
    def initLineEdit(self):
        self.ui.lineEdit_url.setText(self.defaultUrlText)
        labelSearch = QLabel()
        labelSearch.setObjectName("label_search")
        labelSearch.setCursor(Qt.ArrowCursor)
        buttonCollect = QPushButton()
        buttonCollect.setObjectName("pushButton_collect")
        buttonCollect.setCursor(Qt.PointingHandCursor)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,5,0);
        layout.addWidget(labelSearch, 0, Qt.AlignLeft);
        layout.addWidget(buttonCollect, 0, Qt.AlignRight)
        self.ui.lineEdit_url.setLayout(layout);

    # 刷新网页
    def onRefreshClicked(self):
        self.ui.widget_webView.reload()

    # 下一个网页
    def onForwardClicked(self):
        dialog = MessageDialog(self, message="该功能暂时还没有实现，敬请期待！")
        dialog.exec_()

    # 上一个网页
    def onBackwardClicked(self):
        dialog = MessageDialog(self, message="该功能暂时还没有实现，敬请期待！")
        dialog.exec_()

    # 菜单
    def onMenuClicked(self):
        dialog = MessageDialog(self, message="该功能暂时还没有实现，敬请期待！")
        dialog.exec_()

    # 主页
    def onHomePageClicked(self):
        self.ui.widget_webView.load(QUrl("https://www.baidu.com"))

    # 书签
    def onBookmarkClicked(self):
        dialog = MessageDialog(self, message="该功能暂时还没有实现，敬请期待！")
        dialog.exec_()

    # 侧边栏
    def onSlidebarClicked(self):
        dialog = MessageDialog(self, message="该功能暂时还没有实现，敬请期待！")
        dialog.exec_()

    # 最大化
    def onMaxClicked(self):
        if self.isMaximized():
            self.showNormal()
            self.layout().setContentsMargins(1, 1, 1, 1)
            self.ui.pushButton_max.setStyleSheet(ICON_SHOWMAX)
        else:
            self.showMaximized()
            self.layout().setContentsMargins(0, 0, 0, 0)
            self.ui.pushButton_max.setStyleSheet(ICON_SHOWNORMAL)

    # 开始加载网页
    def onLoadStart(self):
        self.ui.pushButton_refresh.setStyleSheet('QPushButton{border-image: url("./resource/icon/cancel.png");}')

    # 加载网页中
    def onLoadProgress(self):
        pass

    # 加载网页完成
    def onLoadFinish(self):
        self.ui.pushButton_refresh.setStyleSheet('QPushButton{border-image: url("./resource/icon/refresh.png");}')

    # 跳转到指定网址
    def onJumpToUrl(self):
        if self.ui.lineEdit_url.text():
            if self.ui.lineEdit_url.text()[0:8] != "https://":
                self.curUrl.setUrl("https://" + self.ui.lineEdit_url.text())
                self.ui.widget_webView.load(self.curUrl)

    # 事件过滤器
    def eventFilter(self, object, event):
        if object == self:
            self.resizeFrame.eventFilter(self, event)
            if event.type() == QEvent.MouseButtonPress:
                self.setFocus()
            # elif event.type() == QEvent.KeyPress:
            #     if event.key() == Qt.Key_F5:
            #         self.ui.widget_webView.reload()
        elif object == self.ui.widget_titleBar:
            self.moveFrame.eventFilter(self, event)
        # 地址栏
        elif object == self.ui.lineEdit_url:
            # FocusIn
            if event.type() == QEvent.FocusIn:
                self.ui.lineEdit_url.setText("")
                self.ui.lineEdit_url.setStyleSheet(INPUT_URL)
            # FocusOut
            elif event.type() == QEvent.FocusOut:
                self.ui.lineEdit_url.setText(self.defaultUrlText)
                self.ui.lineEdit_url.setStyleSheet(LEAVE_URL)
            # 跳转网页
            elif event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Return:
                    self.onJumpToUrl()
                    self.ui.lineEdit_url.clearFocus()
        return False