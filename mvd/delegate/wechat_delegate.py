from PyQt5.QtCore import QSize, QRect, Qt
from PyQt5.QtGui import QPainter, QImage, QFont, QFontMetrics, QBrush, QColor, QPen, QPainterPath
from PyQt5.QtWidgets import QItemDelegate


class WeChatDelegate(QItemDelegate):
    def __init__(self):
        super(WeChatDelegate, self).__init__()
        self.font = QFont("Microsoft YaHei")
        self.font.setPixelSize(14)
        self.font_metric = QFontMetrics(self.font)

    def sizeHint(self, option, index):
        row_count = len(index.data().msg_content)
        height = row_count * 20 + (row_count + 1) * 4 + 10
        if height < 40:
            height = 40
        return QSize(200, height)

    def createEditor(self, parent, option, index):
        pass

    def setEditorData(self, editor, index):
        pass

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def destroyEditor(self, editor, index):
        editor.deleteLater()

    def paint(self, painter, option, index):
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        rect = option.rect
        spacing = 10
        padding_top = 10
        padding_left = 10
        data = index.data()
        is_self = data.is_self

        head_image = QImage(data.head_url).scaled(40, 40, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        if not is_self:
            # 绘制头像
            img_rect = QRect(rect.x(), rect.y(), head_image.width(), head_image.height())
            painter.drawImage(img_rect, head_image)

            # 获取绘制文本信息
            text_len = data.msg_width + padding_left * 2
            bg_rect = QRect(rect.x() + 40 + spacing, rect.y() + padding_top, text_len, rect.height() - padding_top)

            # 绘制背景
            painter.save()
            brush = QBrush(QColor('#ffffff'))
            painter.setBrush(brush)
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(bg_rect, 8, 8)
            path = QPainterPath()
            path.moveTo(bg_rect.x(), bg_rect.y() + 10)
            path.lineTo(bg_rect.x() - 6, bg_rect.y() + 10 + 6)
            path.lineTo(bg_rect.x(), bg_rect.y() + 10 + 12)
            painter.drawPath(path)
            painter.restore()
        else:
            # 绘制头像
            img_rect = QRect(rect.x() + rect.width() - 50, rect.y(), 40, 40)
            painter.drawImage(img_rect, head_image)

            # 获取绘制文本信息
            text_len = data.msg_width + padding_left * 2
            x = rect.width() - 50 - 15 - text_len
            text_len = data.msg_width + padding_left * 2
            bg_rect = QRect(x, rect.y() + padding_top, text_len, rect.height() - padding_top)

            # 绘制背景
            painter.save()
            brush = QBrush(QColor('#ffffff'))
            painter.setBrush(brush)
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(bg_rect, 8, 8)
            path = QPainterPath()
            path.moveTo(bg_rect.x() + bg_rect.width(), bg_rect.y() + 10)
            path.lineTo(bg_rect.x() + bg_rect.width() + 6, bg_rect.y() + 10 + 6)
            path.lineTo(bg_rect.x() + bg_rect.width(), bg_rect.y() + 10 + 12)
            painter.drawPath(path)
            painter.restore()

        # 绘制消息文本
        painter.setFont(self.font)
        for count, text in enumerate(data.msg_content):
            if count == 0:
                y = bg_rect.y() + count * 20 + 5
            else:
                y = bg_rect.y() + count * 20 + (count + 1) * 4
            text_rect = QRect(bg_rect.x()+padding_left, y, bg_rect.width(), 20)
            painter.drawText(text_rect, Qt.AlignLeft | Qt.AlignVCenter, text)
