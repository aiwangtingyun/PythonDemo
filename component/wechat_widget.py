import sys

from PyQt5.QtCore import QSize, Qt, QEvent, QPoint
from PyQt5.QtGui import QTextImageFormat, QTextFormat
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QTextEdit, QPushButton, QStackedWidget

from center.signal_center import SignalCenter
from component.emoji_widget import EmojiWidget
from component.new_message_btn import NewMsgTipButton
from mvd.model.wechat_model import WeChatMsg, WeChatType
from mvd.view.wechat_list_view import WeChatListView


class WeChatWidget(QWidget):
    """ 私聊窗口 """

    def __init__(self, parent=None):
        super(WeChatWidget, self).__init__(parent)
        self.member_width = 200
        self.resize(528 + self.member_width, 642)
        self.setWindowTitle("聊天室")

        self.init_ui()
        self.init_listen()

    def init_ui(self):
        self.setStyleSheet('*{background-color: #CBCFD2;font-family: "Microsoft YaHei";'
                           ' color:#000000; font-size:14px;}')

        self.stack_widget = QStackedWidget(self)
        self.stack_widget.setGeometry(self.member_width, 0, self.width() - self.member_width, self.height())

        widget_chat = QWidget(self)
        widget_chat.resize(self.stack_widget.size())

        # 消息列表视图
        self.list_view = WeChatListView(widget_chat, QSize(528, 502))
        self.list_view.move(0, 0)

        self.new_msg_count = 0

        # 文本输入
        self.text_edit = QTextEdit(widget_chat)
        self.text_edit.setGeometry(0, 502, widget_chat.width(), 140)
        self.text_edit.setPlaceholderText('Enter 发送，Ctrl+Enter 换行')
        self.text_edit.installEventFilter(self)
        self.text_edit.setStyleSheet('''
            QTextEdit{padding-top: 40px;}
        ''')

        # 表情按钮
        self.emoji_btn = QPushButton(self.text_edit)
        self.emoji_btn.setGeometry(3, 3, 32, 32)
        self.emoji_btn.setCursor(Qt.PointingHandCursor)
        self.emoji_btn.clicked.connect(self.popup_emoji_dialog)
        self.emoji_btn.setStyleSheet('''
            QPushButton{border: none; background-image: url(../images/chat_btn_emoji.png); background-color: transparent;}
        ''')

        # 发送消息
        self.send_btn = QPushButton(self.text_edit)
        self.send_btn.setText('发送')
        self.send_btn.setGeometry(self.text_edit.width()-70, self.text_edit.height()-40, 60, 30)
        self.send_btn.clicked.connect(self.on_send_msg)
        self.send_btn.setCursor(Qt.PointingHandCursor)
        self.send_btn.setStyleSheet('''
            QPushButton{background: #157EC9; border-radius: 4px; color: #ffffff;}
            QPushButton:hover{background: #2294E4;}
            QPushButton:pressed{background: #0166AD;}
        ''')

        self.stack_widget.addWidget(widget_chat)
        self.stack_widget.setCurrentIndex(0)

        # 新消息提示按钮
        # self.new_msg_btn = NewMsgTipButton(self)
        # self.new_msg_btn.resize(95, 27)
        # self.new_msg_btn.move(self.list_view.x() + 5, self.list_view.y() + self.list_view.height() - 30)
        # self.new_msg_btn.hide()
        # self.new_msg_btn.button_clicked.connect(self.show_new_msg)

        self.emoji_widget = EmojiWidget()
        self.gender = 1

    def add_chat_widget(self):
        pass

    def init_listen(self):
        SignalCenter().emoji_item_click.connect(self.on_emoji_clicked)

    def eventFilter(self, obj, event):
        """ 事件过滤器，主要过滤回车换行 """
        if obj == self.text_edit:
            if event.type() == QEvent.KeyPress and event.key() in [Qt.Key_Enter, Qt.Key_Return]:
                # ctrl+enter换行
                if QApplication.keyboardModifiers() & Qt.CTRL:
                    cursor = self.text_edit.textCursor()
                    cursor_pos = cursor.position()
                    text = self.text_edit.toPlainText()
                    text = '{}{}{}'.format(text[:cursor_pos], '\n', text[cursor_pos:])
                    self.text_edit.setText(text)
                    cursor.setPosition(cursor_pos + 1)
                    self.text_edit.setTextCursor(cursor)
                else:
                    self.on_send_msg()
                return True
        return False

    def popup_emoji_dialog(self):
        """ 弹出表情选择弹窗 """
        pos = self.mapToGlobal(QPoint(177, self.text_edit.y() - self.emoji_widget.height() + 8))
        self.emoji_widget.move(pos)
        self.emoji_widget.show()

    def on_emoji_clicked(self, data):
        """ 点击 emoji 表情 """
        path = data.get('path')
        code = data.get('code')
        cursor = self.text_edit.textCursor()

        tif = QTextImageFormat()
        tif.setObjectType(QTextFormat.ImageObject)
        tif.setName(path)
        tif.setWidth(16)
        tif.setHeight(16)
        tif.setProperty(Qt.UserRole + 1, code)
        cursor.insertImage(tif)
        self.emoji_widget.hide()

        self.text_edit.setFocus()

    def get_send_content(self):
        """ 获取文本内容 """
        txt = self.text_edit.toPlainText()
        text_arr = txt.split('￼')
        if len(text_arr) <= 1:  # 没有表情直接返回
            return txt

        code_list = []
        for _format in self.text_edit.document().allFormats():
            code = _format.property(Qt.UserRole + 1)
            if code and _format.objectType() == QTextFormat.ImageObject:
                code_list.append('{}'.format(chr(code)))

        content = ''
        for i in range(len(text_arr) - 1):
            if i <= len(code_list) - 1:
                content += text_arr[i] + code_list[i]
            else:
                content += text_arr[i]
        content += text_arr[-1]
        return content

    def on_send_msg(self):
        """ 点击发送 """
        content = self.get_send_content()
        if content == '' or len(content) == 0 or len(content.replace('\n', '')) == 0:
            return

        msg = WeChatMsg()
        msg.msg_content = content
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

        self.text_edit.document().clear()
        self.text_edit.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = WeChatWidget()
    widget.show()

    sys.exit(app.exec_())
