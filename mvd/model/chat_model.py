
# -*- coding: utf-8 -*-
# @Time    : 2020/01/02
# @Author  : wangtingyun
# @Email   : wangtingyun@aipai.com

from PyQt5.QtCore import QAbstractListModel, pyqtSignal, QModelIndex, QVariant, Qt
from PyQt5.QtGui import QImage, QFont, QFontMetrics


class ChatRole:
    Wealth, Vip, Role, Name, Msg, Announce = range(Qt.UserRole, Qt.UserRole + 6)


class ChatModel(QAbstractListModel):
    data_changed = pyqtSignal(int)

    def __init__(self, width=320):
        super(ChatModel, self).__init__()
        self.font = QFont('Microsoft YaHei')
        self.font.setPixelSize(14)
        self.font_metric = QFontMetrics(self.font)
        self.msg_width = width - 12 - 16 - 20
        self._data_list = []

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._data_list)

    def add_data(self, data):
        self._data_list.append(data)
        self.beginInsertRows(QModelIndex(), self.rowCount()-1, self.rowCount()-1)
        self.endInsertRows()
        self.data_changed.emit(len(self._data_list)-1)

    def data(self, index, role=None):
        item = self._data_list[index.row()]
        if role:
            return QVariant
        else:
            return item

    def add_announce(self, announce):
        all_row_contents = []
        row_contents = []
        single_msg = ''

        # 公告头
        item_msg = {'type': ChatRole.Announce, 'content': announce.title}
        row_contents.append(item_msg.copy())
        all_row_contents.append(row_contents.copy())
        row_contents.clear()

        # 公告内容
        for count, i in enumerate(announce.content):
            single_msg += i
            msg_len = self.font_metric.boundingRect(single_msg).width()
            if msg_len >= self.msg_width or i == '\n':
                item_msg['content'] = single_msg[:]
                row_contents.append(item_msg.copy())
                all_row_contents.append(row_contents.copy())
                row_contents.clear()
                single_msg = ''
            if count == len(announce.content) - 1 and single_msg:
                item_msg['content'] = single_msg[:]
                row_contents.append(item_msg.copy())
                all_row_contents.append(row_contents.copy())
                row_contents.clear()
                single_msg = ''

        model_data = {'width': msg_len, 'row': len(all_row_contents) + 2, 'data': all_row_contents}

        self.add_data(model_data)

    def add_like_emiji(self, msg):
        all_row_contents = []
        row_contents = []
        single_msg = ''
        image_len = 0
        image_space = 6
        item_msg = {'type': 0, 'content': None}

        # (财富+VIP+角色)图片确保不占满一行
        if msg.vip:
            item_msg['type'] = ChatRole.Vip
            item_msg['content'] = QImage('./image/vip.png')
            image_len += item_msg['content'].width() + image_space
            row_contents.append(item_msg.copy())
        if msg.role > 0:
            item_msg['type'] = ChatRole.Role
            if msg.role == 1:
                item_msg['content'] = QImage('./image/boss.png')
            elif msg.role == 2:
                item_msg['content'] = QImage('./image/host.png')
            image_len += item_msg['content'].width() + image_space
            row_contents.append(item_msg.copy())

        # 前面的图片加上昵称可能占满一行也可能不占满一行
        name = msg.nickname + ' : ' + '              '
        item_msg['type'] = ChatRole.Msg
        for count, i in enumerate(name):
            single_msg += i
            msg_len = self.font_metric.boundingRect(single_msg).width() + image_len
            if msg_len >= self.msg_width:
                item_msg['content'] = single_msg[:]
                row_contents.append(item_msg.copy())
                all_row_contents.append(row_contents.copy())
                row_contents.clear()
                single_msg = ''
            if count == len(name)-1:
                item_msg['content'] = single_msg[:]
                row_contents.append(item_msg.copy())

        all_row_contents.append(row_contents)
        model_data = {'type': 'webp', 'width': msg_len, 'row': len(all_row_contents)+2, 'data': all_row_contents}

        self.add_data(model_data)

    def split_msg(self, msg):
        all_row_contents = []
        row_contents = []
        single_msg = ''
        image_len = 0
        image_space = 6
        item_msg = {'type': 0, 'content': None}

        # (财富+VIP+角色)图片确保不占满一行
        if msg.vip:
            item_msg['type'] = ChatRole.Vip
            item_msg['content'] = QImage('./image/vip.png')
            image_len += item_msg['content'].width() + image_space
            row_contents.append(item_msg.copy())
        if msg.role > 0:
            item_msg['type'] = ChatRole.Role
            if msg.role == 1:
                item_msg['content'] = QImage('./image/boss.png')
            elif msg.role == 2:
                item_msg['content'] = QImage('./image/host.png')
            image_len += item_msg['content'].width() + image_space
            row_contents.append(item_msg.copy())

        # 前面的图片加上昵称可能占满一行也可能不占满一行
        name = msg.nickname + ' :  '
        item_msg['type'] = ChatRole.Msg
        for i in name:
            single_msg += i
            msg_len = self.font_metric.boundingRect(single_msg).width() + image_len
            if msg_len >= self.msg_width:
                item_msg['content'] = single_msg[:]
                row_contents.append(item_msg.copy())
                all_row_contents.append(row_contents.copy())
                row_contents.clear()
                single_msg = ''

        # 剩下的就是消息内容了
        for count, i in enumerate(msg.msg):
            single_msg += i
            image_len = 0 if all_row_contents else image_len
            msg_len = self.font_metric.boundingRect(single_msg).width() + image_len
            if msg_len >= self.msg_width or i == '\n':
                item_msg['content'] = single_msg[:]
                row_contents.append(item_msg.copy())
                all_row_contents.append(row_contents.copy())
                row_contents.clear()
                single_msg = ''
            if count == len(msg.msg) - 1 and single_msg:
                item_msg['content'] = single_msg[:]
                row_contents.append(item_msg.copy())
                all_row_contents.append(row_contents.copy())
                row_contents.clear()
                single_msg = ''

        return all_row_contents
