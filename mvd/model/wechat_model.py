from PyQt5.QtCore import QAbstractListModel, QVariant, QModelIndex, Qt
from PyQt5.QtGui import QFont, QFontMetrics


class WeChatType:
    Text, Emoji, Image = range(Qt.UserRole, Qt.UserRole + 3)


class WeChatMsg:
    def __init__(self):
        self.head_url = ''
        self.msg_type = ''
        self.msg_content = ''
        self.msg_width = 20
        self.is_self = False


class WeChatModel(QAbstractListModel):
    def __init__(self):
        super(WeChatModel, self).__init__()
        self._data_list = []
        self.max_width = 100
        self.font = QFont("Microsoft YaHei")
        self.font.setPixelSize(14)
        self.font_metric = QFontMetrics(self.font)

    def set_max_width(self, width):
        self.max_width = width

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._data_list)

    def data(self, index, role=None):
        item = self._data_list[index.row()]
        if role:
            return QVariant
        else:
            return item

    def add_data(self, data):

        if data.msg_type == WeChatType.Text:
            self.add_text_msg(data)

        self._data_list.append(data)
        self.beginInsertRows(QModelIndex(), self.rowCount()-1, self.rowCount()-1)
        self.endInsertRows()
        # self.data_changed.emit(len(self._data_list)-1)

    def add_text_msg(self, data):
        line_text = ''
        text_content = []
        for count, char in enumerate(data.msg_content):
            line_text += char
            line_len = self.font_metric.width(line_text)
            if line_len >= self.max_width:
                text_content.append(line_text[:])
                line_len = 0
                line_text = ''
            if count == len(data.msg_content) - 1 and line_text:
                text_content.append(line_text[:])
        data.msg_width = self.font_metric.width(text_content[0])
        data.msg_content = text_content.copy()
