# -*- coding: utf-8 -*-
# @Time    : 2020/01/02
# @Author  : wangtingyun
# @Email   : wangtingyun@aipai.com

from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QFont, QFontMetrics


class EmojiTextPainter(QObject):
    '''绘制文字和emoji夹杂在一起的文本'''

    def __init__(self, font_sizes=None):
        super(EmojiTextPainter, self).__init__()

        # 构建字体库
        self.font_lib = {}
        if not font_sizes:
            font_sizes = [14]
        for font_size in font_sizes:
            normal_font = QFont('Microsoft YaHei')
            normal_font.setPixelSize(font_size)
            normal_font_metrics = QFontMetrics(normal_font)
            emoji_font = QFont('Segoe UI Emoji')
            emoji_font.setPixelSize(font_size)
            emoji_font_metrics = QFontMetrics(emoji_font)
            self.font_lib[font_size] = {
                'normal_font': normal_font, 'normal_font_metrics': normal_font_metrics,
                'emoji_font': emoji_font, 'emoji_font_metrics': emoji_font_metrics
            }

        # 构建绘制位置
        self.left = 'left'
        self.center = 'center'

    def is_emoji(self, character):
        '''过滤特殊字符字符'''

        unicode = ord(character)
        # 中文
        if unicode in range(0x4E00, 0x9FA5 + 1):
            return False
        # ascii
        elif unicode in range(0x000, 0x0FF + 1):
            return False
        # 标点符号
        elif unicode in [
                0x3002, 0xFF1F, 0xFF01, 0x3010, 0x3011, 0xFF0C, 0x3001, 0xFF1B,
                0xFF1A, 0x300C, 0x300D, 0x300E, 0x300F, 0x2019, 0x201C, 0x201D,
                0x2018, 0xFF08, 0xFF09, 0x3014, 0x3015, 0x2026, 0x2013, 0xFF0E,
                0x2014, 0x300A, 0x300B, 0x3008, 0x3009]:
            return False
        else:
            return True

    def split_text(self, text):
        '''分割emoji字符串'''

        emoji_texts = []
        item_text = {}

        for index, ch in enumerate(text):
            text_type = self.is_emoji(ch)
            if index == 0:
                item_text = {'type': text_type, 'text': ch}
            else:
                if item_text['type'] == text_type:
                    item_text['text'] += ch
                else:
                    emoji_texts.append(item_text.copy())
                    item_text = {'type': text_type, 'text': ch}
            if index == len(text) - 1:
                emoji_texts.append(item_text.copy())

        return emoji_texts

    def draw_text(self, painter, rect, text, font_size, align=None):
        # 选择字体
        normal_font = self.font_lib[font_size]['normal_font']
        emoji_font = self.font_lib[font_size]['emoji_font']
        normal_font_metrics = self.font_lib[font_size]['normal_font_metrics']
        emoji_font_metrics = self.font_lib[font_size]['emoji_font_metrics']

        # 调节绘制的初始位置
        draw_pos = 0
        if align and align == self.center:
            draw_pos = (rect.width() - normal_font_metrics.boundingRect(text).width()) // 2

        # 分离字符串
        draw_texts = self.split_text(text)

        # 绘制字符串
        painter.save()
        for item in draw_texts:
            if item['type']:
                painter.setFont(emoji_font)
                painter.drawText(rect.x() + draw_pos - 3, rect.y() - 2, rect.width(), rect.height(),
                                 Qt.AlignLeft | Qt.AlignTop, item['text'])
                draw_pos += emoji_font_metrics.boundingRect(item['text']).width() + 1
            else:
                painter.setFont(normal_font)
                painter.drawText(rect.x() + draw_pos, rect.y(), rect.width(), rect.height(),
                                 Qt.AlignLeft | Qt.AlignTop, item['text'])
                draw_pos += normal_font_metrics.boundingRect(item['text']).width() + 1
        painter.restore()

    def draw_text_2(self, painter, rect, texts, font_size, origin_text='', align=None):
        '''
        这个版本是提供于已经提前切割好字符串的情况，为了加快性能
        如果想要支持居中对齐，需要提供未切割前的字符串
        '''

        # 选择字体
        normal_font = self.font_lib[font_size]['normal_font']
        emoji_font = self.font_lib[font_size]['emoji_font']
        normal_font_metrics = self.font_lib[font_size]['normal_font_metrics']
        emoji_font_metrics = self.font_lib[font_size]['emoji_font_metrics']

        # 调节绘制的初始位置
        draw_pos = 0
        if align and align == self.center:
            draw_pos = (rect.width() - normal_font_metrics.boundingRect(origin_text).width()) // 2

        # 绘制字符串
        painter.save()
        for item in texts:
            if item['type']:
                painter.setFont(emoji_font)
                painter.drawText(rect.x() + draw_pos - 3, rect.y() - 2, rect.width(), rect.height(),
                                 Qt.AlignLeft | Qt.AlignTop, item['text'])
                draw_pos += emoji_font_metrics.boundingRect(item['text']).width() + 1
            else:
                painter.setFont(normal_font)
                painter.drawText(rect.x() + draw_pos, rect.y(), rect.width(), rect.height(),
                                 Qt.AlignLeft | Qt.AlignTop, item['text'])
                draw_pos += normal_font_metrics.boundingRect(item['text']).width() + 1
        painter.restore()

    def get_text_len(self, texts, font_size):
        '''传进来的texts必须是已经切割好的字符串'''

        # 选择字体
        normal_font_metrics = self.font_lib[font_size]['normal_font_metrics']
        emoji_font_metrics = self.font_lib[font_size]['emoji_font_metrics']

        # 计算字符串长度
        text_len = 0
        for item in texts:
            if item['type']:
                text_len += emoji_font_metrics.boundingRect(item['text']).width() + 1
            else:
                text_len += normal_font_metrics.boundingRect(item['text']).width() + 1
        return text_len
