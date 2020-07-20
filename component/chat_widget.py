# -*- coding: utf-8 -*-
# @Time    : 2020/01/02
# @Author  : wangtingyun
# @Email   : wangtingyun@aipai.com

import random

import sys
from PyQt5.QtCore import Qt, QEvent, QTimer
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QLabel, QApplication

from component.new_message_btn import NewMsgTipButton
from mvd.view.chat_list_view import ChatListView


class Announce:
    def __init__(self):
        self.title = '★温馨提示★'
        self.content = '欢迎来到💘廷云🌸空间✨欢迎来到💘廷云🌸空间✨\n🌸🌸🌸🌸🌸🌸🌸🌸🌸'


class MsgData:
    def __init__(self):
        self.nickname = '💘廷云🌸空间✨'
        self.wealth = 10
        self.vip = 1
        self.role = 1
        self.msg = 'hello python'


class ChatWidget(QWidget):

    def __init__(self, parent=None, width=528, height=602):
        super(ChatWidget, self).__init__(parent)
        self.setWindowTitle('聊天室')
        self.resize(width, height)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet('*{background-color:#ff243A55;font-family: "Microsoft YaHei";'
                           ' color:#ffffff; font-size:14px;}')

        # 消息列表视图
        self.list_view = ChatListView(self, 528, 472)
        self.list_view.move(0, 30)
        self.list_view.has_new_msg.connect(self.has_new_msg)
        self.list_view.scroll_to_bottom.connect(self.has_new_msg)

        self.new_msg_count = 0

        # 提示条
        self.tip = QLabel(self)
        self.tip.setGeometry(0, 0, self.width(), 30)
        self.tip.setAlignment(Qt.AlignCenter)
        self.tip.setStyleSheet('QLabel{font-size:16px; color:#FF7C45;}')
        self.tip.setText('聊天室面板')

        # 文本输入
        self.text_input = QTextEdit(self)
        self.text_input.setGeometry(0, 502, 480, 100)
        self.text_input.setPlaceholderText('Enter 发送，Ctrl+Enter 换行')
        self.text_input.installEventFilter(self)

        # 发送消息
        self.send_btn = QPushButton(self)
        self.send_btn.setText('发送')
        self.send_btn.setGeometry(480, 502, 55, 100)
        self.send_btn.clicked.connect(self.on_send_msg)

        # 新消息提示按钮
        self.new_msg_btn = NewMsgTipButton(self)
        self.new_msg_btn.setGeometry(self.list_view.x()+5, self.list_view.y()+self.list_view.height()-30, 95, 27)
        self.new_msg_btn.hide()
        self.new_msg_btn.button_clicked.connect(self.show_new_msg)

        self.list_view.model.add_announce(Announce())

        # self.count = 0
        # self.test_performance()

    def test_performance(self):
        index = random.randint(0, 2)
        msgs = ['V.m🌸晚吟✨老鱼小仙女🐷', '小甜甜💘.', '大静静🌹宠爱娱乐厅11860晚上7.30拍卖会']
        msg = MsgData()
        msg.msg = msgs[index]
        self.list_view.add_msg(msg)
        self.count += 1
        if self.count < 20:
            QTimer.singleShot(200, self.test_performance)

    def eventFilter(self, obj, event):
        if obj == self.text_input:
            if event.type() == QEvent.KeyPress and event.key() in [Qt.Key_Enter, Qt.Key_Return]:
                # ctrl+enter换行
                if QApplication.keyboardModifiers() & Qt.CTRL:
                    cursor = self.text_input.textCursor()
                    cursor_pos = cursor.position()
                    text = self.text_input.toPlainText()
                    text = '{}{}{}'.format(text[:cursor_pos], '\n', text[cursor_pos:])
                    self.text_input.setText(text)
                    cursor.setPosition(cursor_pos + 1)
                    self.text_input.setTextCursor(cursor)
                else:
                    self.on_send_msg()
                return True
        return False

    def show_new_msg(self):
        self.list_view.scrollToBottom()
        self.new_msg_btn.hide()
        self.new_msg_count = 0

    def has_new_msg(self):
        if not self.list_view.is_at_bottom:
            if self.new_msg_count < 99:
                self.new_msg_count += 1
            self.new_msg_btn.set_msg_count(self.new_msg_count)
            self.new_msg_btn.show()
        else:
            self.list_view.scrollToBottom()
            self.new_msg_btn.hide()
            self.new_msg_count = 0

    def on_send_msg(self):
        text = self.text_input.toPlainText()
        if text:
            msg = MsgData()
            msg.msg = text
            self.list_view.add_msg(msg)
            # self.list_view.model.add_like_emiji(msg)
            self.text_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ChatWidget()
    widget.show()
    sys.exit(app.exec_())
