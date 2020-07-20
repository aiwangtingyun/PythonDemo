from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListView, QAbstractItemView

from mvd.delegate.wechat_delegate import WeChatDelegate
from mvd.model.wechat_model import WeChatModel


class WeChatListView(QListView):
    def __init__(self, parent=None, size=None):
        super(WeChatListView, self).__init__(parent)
        if size and isinstance(size, QSize):
            self.resize(size)
        self.setViewMode(QListView.ListMode)
        self.setSpacing(3)
        self._model = WeChatModel()
        self._model.set_max_width(350)
        self._delegate = WeChatDelegate()

        self.setModel(self._model)
        self.setItemDelegate(self._delegate)

        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.verticalScrollBar().setVisible(False)
        self.verticalScrollBar().setStyleSheet("QScrollBar:vertical{width:0px;}")

    def add_msg(self, msg):
        self._model.add_data(msg)
        self.scrollToBottom()
