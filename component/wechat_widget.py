import sys

from PyQt5.QtCore import QSize, Qt, QEvent
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QTextEdit, QPushButton

from component.new_message_btn import NewMsgTipButton
from mvd.model.wechat_model import WeChatMsg, WeChatType
from mvd.view.wechat_list_view import WeChatListView


class WeChatWidget(QWidget):
    """ 私聊窗口 """

    def __init__(self, parent=None):
        super(WeChatWidget, self).__init__(parent)
        self.resize(528, 602)
        self.setWindowTitle("聊天窗口")
        self.setStyleSheet('*{background-color: #CBCFD2;font-family: "Microsoft YaHei";'
                           ' color:#000000; font-size:14px;}')

        # 消息列表视图
        self.list_view = WeChatListView(self, QSize(528, 472))
        self.list_view.move(0, 30)

        self.new_msg_count = 0

        # 提示条
        self.tip = QLabel(self)
        self.tip.setGeometry(0, 0, self.width(), 30)
        self.tip.setAlignment(Qt.AlignCenter)
        self.tip.setStyleSheet('QLabel{font-size:16px; color:#000000;}')
        self.tip.setText('私聊面板')

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

        self.gender = 1

        # 新消息提示按钮
        # self.new_msg_btn = NewMsgTipButton(self)
        # self.new_msg_btn.setGeometry(self.list_view.x() + 5, self.list_view.y() + self.list_view.height() - 30, 95, 27)
        # self.new_msg_btn.hide()
        # self.new_msg_btn.button_clicked.connect(self.show_new_msg)

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

    def on_send_msg(self):
        text = self.text_input.toPlainText()
        if text:
            msg = WeChatMsg()
            msg.msg_content = text
            msg.msg_type = WeChatType.Text
            if self.gender == 1:
                msg.head_url = '../images/head_man.png'
                self.gender = 2
                msg.is_self = False
            else:
                self.gender = 1
                msg.is_self = True
                msg.head_url = '../images/head_woman.png'
            self.list_view.add_msg(msg)
            self.text_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = WeChatWidget()
    widget.show()

    sys.exit(app.exec_())
