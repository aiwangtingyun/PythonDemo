# -*- coding: utf-8 -*-
# @Time    : 2020/01/02
# @Author  : wangtingyun
# @Email   : wangtingyun@aipai.com

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QListView, QAbstractItemView

from mvd.delegate.chat_delegate import ChatDelegate
from mvd.model.chat_model import ChatModel


class ChatListView(QListView):
    has_new_msg = pyqtSignal()
    scroll_to_bottom = pyqtSignal()

    def __init__(self, parent=None, width=320, height=160):
        super(ChatListView, self).__init__(parent)
        self.setViewMode(QListView.ListMode)
        self.setSpacing(3)
        self.resize(width, height)

        self.is_at_bottom = False

        self.model = ChatModel(width)
        self.model.data_changed.connect(self.model_data_changed)
        self.setModel(self.model)

        self.delegate = ChatDelegate()
        self.delegate.set_max_width(width)
        self.setItemDelegate(self.delegate)

        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.verticalScrollBar().setVisible(False)
        self.verticalScrollBar().valueChanged.connect(self.check_at_bottom)
        self.verticalScrollBar().setStyleSheet("QScrollBar:vertical{width:0px;}")

    def model_data_changed(self, index):
        self.openPersistentEditor(self.model.index(index))

    def check_at_bottom(self):
        if self.verticalScrollBar().value() == self.verticalScrollBar().maximum():
            self.is_at_bottom = True
            self.scroll_to_bottom.emit()
        else:
            self.is_at_bottom = False

    def add_msg(self, msg):
        self.check_at_bottom()
        msg = self.split_msg(msg)
        self.model.add_data(msg)
        self.has_new_msg.emit()
