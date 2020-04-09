# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'material_tip_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 387)
        self.widget_titleBar = QtWidgets.QWidget(Dialog)
        self.widget_titleBar.setGeometry(QtCore.QRect(10, 10, 720, 32))
        self.widget_titleBar.setObjectName("widget_titleBar")
        self.label = QtWidgets.QLabel(self.widget_titleBar)
        self.label.setGeometry(QtCore.QRect(17, 10, 54, 12))
        self.label.setStyleSheet("QLabel {\n"
"font-family:\"Microsoft YaHei\";\n"
"font-size:12px;\n"
"color:#BDC8E2;\n"
"background:transparent;\n"
"}")
        self.label.setObjectName("label")
        self.pushButton_close = QtWidgets.QPushButton(self.widget_titleBar)
        self.pushButton_close.setGeometry(QtCore.QRect(692, 10, 14, 14))
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.label_sep1 = QtWidgets.QLabel(Dialog)
        self.label_sep1.setGeometry(QtCore.QRect(10, 43, 720, 1))
        self.label_sep1.setStyleSheet("QLabel{\n"
"background:#151921;\n"
"}")
        self.label_sep1.setText("")
        self.label_sep1.setObjectName("label_sep1")
        self.label_sep2 = QtWidgets.QLabel(Dialog)
        self.label_sep2.setGeometry(QtCore.QRect(10, 44, 720, 1))
        self.label_sep2.setStyleSheet("QLabel{\n"
"background:#272D3D;\n"
"}")
        self.label_sep2.setText("")
        self.label_sep2.setObjectName("label_sep2")
        self.widget_body = QtWidgets.QWidget(Dialog)
        self.widget_body.setGeometry(QtCore.QRect(10, 45, 720, 333))
        self.widget_body.setObjectName("widget_body")
        self.pushButton_ok = QtWidgets.QPushButton(self.widget_body)
        self.pushButton_ok.setGeometry(QtCore.QRect(344, 293, 52, 24))
        self.pushButton_ok.setStyleSheet("QPushButton {\n"
"font-family:\"Microsoft YaHei\";\n"
"font-size:12px;\n"
"background-color:#2E3648;\n"
"color:#BDC8E2;\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:#384156;\n"
"color:#BDC8E2;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#292F3F;\n"
"color:#737E9E;\n"
"}")
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.widget_content = QtWidgets.QWidget(self.widget_body)
        self.widget_content.setGeometry(QtCore.QRect(16, 16, 688, 261))
        self.widget_content.setObjectName("widget_content")
        self.widget_listHead = QtWidgets.QWidget(self.widget_content)
        self.widget_listHead.setGeometry(QtCore.QRect(1, 1, 686, 32))
        self.widget_listHead.setStyleSheet("QWidget {\n"
"background-color:#212735;\n"
"}")
        self.widget_listHead.setObjectName("widget_listHead")
        self.label_2 = QtWidgets.QLabel(self.widget_listHead)
        self.label_2.setGeometry(QtCore.QRect(149, 10, 54, 12))
        self.label_2.setStyleSheet("QLabel {\n"
"font-family:\"Microsoft YaHei\";\n"
"font-size:12px;\n"
"color:#BDC8E2;\n"
"background:transparent;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_listHead)
        self.label_3.setGeometry(QtCore.QRect(492, 10, 54, 12))
        self.label_3.setStyleSheet("QLabel {\n"
"font-family:\"Microsoft YaHei\";\n"
"font-size:12px;\n"
"color:#BDC8E2;\n"
"background:transparent;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_listHead)
        self.label_4.setGeometry(QtCore.QRect(343, 6, 1, 20))
        self.label_4.setStyleSheet("QLabel{\n"
"background-color:#151921;\n"
"}")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.listWidget = QtWidgets.QListWidget(self.widget_content)
        self.listWidget.setGeometry(QtCore.QRect(1, 33, 686, 228))
        self.listWidget.setStyleSheet("QListWidget {\n"
"background-color:#151921;\n"
"}")
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "修复素材"))
        self.pushButton_ok.setText(_translate("Dialog", "确定"))
        self.label_2.setText(_translate("Dialog", "无效素材"))
        self.label_3.setText(_translate("Dialog", "替换素材"))

