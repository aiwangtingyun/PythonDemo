# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(736, 616)
        self.verticalLayout = QtWidgets.QVBoxLayout(main_window)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_titleBar = QtWidgets.QWidget(main_window)
        self.widget_titleBar.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_titleBar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_titleBar.setObjectName("widget_titleBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_titleBar)
        self.horizontalLayout_3.setContentsMargins(4, 0, 12, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_logo = QtWidgets.QLabel(self.widget_titleBar)
        self.label_logo.setMinimumSize(QtCore.QSize(25, 0))
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_2.addWidget(self.label_logo)
        self.label_appName = QtWidgets.QLabel(self.widget_titleBar)
        self.label_appName.setMinimumSize(QtCore.QSize(50, 0))
        self.label_appName.setLineWidth(1)
        self.label_appName.setObjectName("label_appName")
        self.horizontalLayout_2.addWidget(self.label_appName)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(281, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setContentsMargins(10, -1, 0, -1)
        self.horizontalLayout_1.setSpacing(12)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.pushButton_min = QtWidgets.QPushButton(self.widget_titleBar)
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.horizontalLayout_1.addWidget(self.pushButton_min)
        self.pushButton_max = QtWidgets.QPushButton(self.widget_titleBar)
        self.pushButton_max.setText("")
        self.pushButton_max.setObjectName("pushButton_max")
        self.horizontalLayout_1.addWidget(self.pushButton_max)
        self.pushButton_close = QtWidgets.QPushButton(self.widget_titleBar)
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_1.addWidget(self.pushButton_close)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_1)
        self.verticalLayout.addWidget(self.widget_titleBar)
        self.widget_menu = QtWidgets.QWidget(main_window)
        self.widget_menu.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_menu.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_menu.setObjectName("widget_menu")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_menu)
        self.horizontalLayout_6.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_back = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_back.setText("")
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout_4.addWidget(self.pushButton_back)
        self.pushButton_forward = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_forward.setText("")
        self.pushButton_forward.setObjectName("pushButton_forward")
        self.horizontalLayout_4.addWidget(self.pushButton_forward)
        self.pushButton_refresh = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_refresh.setText("")
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout_4.addWidget(self.pushButton_refresh)
        self.pushButton_home = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_home.setText("")
        self.pushButton_home.setObjectName("pushButton_home")
        self.horizontalLayout_4.addWidget(self.pushButton_home)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.lineEdit_url = QtWidgets.QLineEdit(self.widget_menu)
        self.lineEdit_url.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout_6.addWidget(self.lineEdit_url)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_bookmark = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_bookmark.setText("")
        self.pushButton_bookmark.setObjectName("pushButton_bookmark")
        self.horizontalLayout_5.addWidget(self.pushButton_bookmark)
        self.pushButton_slidebar = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_slidebar.setText("")
        self.pushButton_slidebar.setObjectName("pushButton_slidebar")
        self.horizontalLayout_5.addWidget(self.pushButton_slidebar)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_sep1 = QtWidgets.QLabel(self.widget_menu)
        self.label_sep1.setMaximumSize(QtCore.QSize(1, 16777215))
        self.label_sep1.setText("")
        self.label_sep1.setObjectName("label_sep1")
        self.horizontalLayout_8.addWidget(self.label_sep1)
        self.pushButton_menu = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_menu.setText("")
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.horizontalLayout_8.addWidget(self.pushButton_menu)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.widget_menu)
        self.widget_body = QtWidgets.QWidget(main_window)
        self.widget_body.setObjectName("widget_body")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_body)
        self.gridLayout.setContentsMargins(0, 0, 3, 3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_webView = QtWebEngineWidgets.QWebEngineView(self.widget_body)
        self.widget_webView.setObjectName("widget_webView")
        self.gridLayout.addWidget(self.widget_webView, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_body)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Form"))
        self.widget_titleBar.setWhatsThis(_translate("main_window", "mainWindowTitleBar"))
        self.label_logo.setText(_translate("main_window", "Logo"))
        self.label_appName.setText(_translate("main_window", "AppName"))

from PyQt5 import QtWebEngineWidgets
