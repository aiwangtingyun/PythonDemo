from PyQt5.QtCore import pyqtSignal, QObject

from tools.decorator_tool import singleton


@singleton
class SignalCenter(QObject):
    """
    全局信号模块
    """
    emoji_item_click = pyqtSignal(dict)
