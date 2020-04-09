# -*- coding: utf-8 -*-
# @Time    : 2020/01/02
# @Author  : wangtingyun
# @Email   : wangtingyun@aipai.com

from PyQt5.QtCore import QSize, QRect, Qt
from PyQt5.QtGui import QFontMetrics, QFont, QBrush, QColor, QPainter, QPen
from PyQt5.QtWidgets import QWidget, QPushButton, QStyledItemDelegate

from component.emoji_text_painter import EmojiTextPainter
from component.movie_player import MoviePlayer
from mvd.model.chat_model import ChatRole


class ChatEditor(QWidget):

    def __init__(self, parent=None):
        super(ChatEditor, self).__init__(parent)
        self.btn_show_announce = QPushButton(self)
        self.btn_show_announce.setText('查看房间公告 >')
        self.btn_show_announce.setStyleSheet('''
            QPushButton{font-family:"Microsoft YaHei"; font-size: 12px; color:#63BEFF; 
                        background-color: transparent; border: none; }
            QPushButton:hover{color:#2294E4;}
            QPushButton:pressed{color:#0166AD;}
        ''')

    def resizeEvent(self, event):
        self.btn_show_announce.setGeometry(self.width() - 100 - 16, self.height() - 20 - 12, 100, 20)


class ChatDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        super(ChatDelegate, self).__init__(parent)
        self.emoji_painter = EmojiTextPainter([14])
        self.max_width = 100
        self.single_row_height = 32
        self.font = QFont('Microsoft YaHei')
        self.font.setPixelSize(14)
        self.font_metric = QFontMetrics(self.font)

    def set_max_width(self, width):
        self.max_width = width - 10

    def sizeHint(self, option, index):
        return QSize(100, self.single_row_height + 20 * (index.data()['row'] - 1))

    def createEditor(self, parent, option, index):
        if index.row() == 0:
            editor = ChatEditor(parent)
        else:
            if index.data()['type'] == 'webp':
                editor = MoviePlayer(parent)
                editor.set_movie_path('./webp/like.webp')
                editor.start_movie()
        return editor

    def destroyEditor(self, editor, index):
        editor.deleteLater()

    def setEditorData(self, editor, index):
        if index.row() != 0:
            editor.set_data(index.data().get('width', ''))

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def paint_announce(self, painter, rect, announce):
        padding_left = 12

        # 绘制公告内容
        for count, row in enumerate(announce):
            if count == 0:
                title_rect = QRect(rect.x() + padding_left, rect.y(), self.max_width, self.single_row_height)
                painter.drawText(title_rect, Qt.AlignCenter, row[0]['content'])
            elif count == len(announce):
                pass
            else:
                for item in row:
                    y = rect.y() + self.single_row_height + (count - 1) * 20
                    content_rect = QRect(rect.x() + padding_left, y, self.max_width, self.single_row_height)
                    # painter.drawText(content_rect, Qt.AlignLeft, item['content'])
                    self.emoji_painter.draw_text(painter, content_rect, item['content'], 14, 'left')

        # 绘制背景
        brush = QBrush(QColor('#13ffffff'))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        back_rect = QRect(rect.x(), rect.y(), self.max_width, rect.height())
        painter.drawRoundedRect(back_rect, 16, 16)

    def paint(self, painter, option, index):
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        rect = option.rect
        padding_left = 12
        padding_right = 16
        padding_top = 5
        image_space = 6

        pen = QPen(QColor('#ffcc00'))
        pen.setColor(QColor('#ffffff'))
        painter.setPen(pen)
        painter.setFont(self.font)

        # 绘制公告
        if index.row() == 0:
            self.paint_announce(painter, rect, index.data()['data'])
            return

        # 绘制消息内容
        max_len = 0
        for count, row in enumerate(index.data()['data']):
            content_len = 0
            for item in row:
                x = rect.x() + padding_left + content_len
                if item['type'] != ChatRole.Msg:
                    img = item['content']
                    y = rect.y() + (self.single_row_height - img.height()) // 2
                    img_rect = QRect(x, y, img.width(), img.height())
                    painter.drawImage(img_rect, img)
                    content_len += img.width() + image_space
                else:
                    msg = item['content']
                    y = rect.y() + padding_top + count * 20
                    msg_len = self.font_metric.boundingRect(msg).width()
                    msg_rect = QRect(x, y, msg_len, self.single_row_height)
                    # painter.drawText(msg_rect, Qt.AlignCenter, msg)
                    self.emoji_painter.draw_text(painter, msg_rect, msg, 14, 'left')
                    content_len += msg_len
                    max_len = content_len if content_len > max_len else max_len

        # 绘制背景
        brush = QBrush(QColor('#13ffffff'))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        back_width = padding_left + max_len + padding_right
        back_width = self.max_width if back_width > self.max_width else back_width
        back_rect = QRect(rect.x(), rect.y(), back_width, rect.height())
        painter.drawRoundedRect(back_rect, 16, 16)